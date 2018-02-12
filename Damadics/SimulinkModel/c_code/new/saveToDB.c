/*
 * sfuntmpl_basic.c: Basic 'C' template for a level 2 S-function.
 *
 * Copyright 1990-2013 The MathWorks, Inc.
 */


/*
 * You must specify the S_FUNCTION_NAME as the name of your S-function
 * (i.e. replace sfuntmpl_basic with the name of your S-function).
 */

#define S_FUNCTION_NAME  saveToDB
#define S_FUNCTION_LEVEL 2

/*
 * Need to include simstruc.h for the definition of the SimStruct and
 * its associated macro definitions.
 */
#include "simstruc.h"

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <mysql.h>
#include "utils.h"

#define INPUT_PARAMS 4

int connect_to_DB(char *, char *, char *, char *);
int writeToDB(time_t);
void updateSensorValues(const real_T *);
int initValues(SimStruct *S);

typedef struct
{
  double controlValue;
  double pressureValveInlet;
  double pressureValveOutlet;
  double rodDisplacement;
  double disturbedMediumFlow;
  double mediumTemperature;
  double faultIntensity;
  int selectedFault;
  int faultType;
} damadicsSensorValues;

MYSQL *con;
damadicsSensorValues sensorValues;
int alreadySampled;
time_t startDateTime;
FILE *startDateTimeFile, *logFile;
unsigned long lastSampleTime;
int stopFlag, connectionUp;


/* Error handling
 * --------------
 *
 * You should use the following technique to report errors encountered within
 * an S-function:
 *
 *       ssSetErrorStatus(S,"Error encountered due to ...");
 *       return;
 *
 * Note that the 2nd argument to ssSetErrorStatus must be persistent memory.
 * It cannot be a local variable. For example the following will cause
 * unpredictable errors:
 *
 *      mdlOutputs()
 *      {
 *         char msg[256];         {ILLEGAL: to fix use "static char msg[256];"}
 *         sprintf(msg,"Error due to %s", string);
 *         ssSetErrorStatus(S,msg);
 *         return;
 *      }
 *
 */

/*====================*
 * S-function methods *
 *====================*/

/* Function: mdlInitializeSizes ===============================================
 * Abstract:
 *    The sizes information is used by Simulink to determine the S-function
 *    block's characteristics (number of inputs, outputs, states, etc.).
 */
static void mdlInitializeSizes(SimStruct *S)
{
    ssSetNumSFcnParams(S, INPUT_PARAMS);  /* Number of expected parameters */
    if (ssGetNumSFcnParams(S) != ssGetSFcnParamsCount(S)) {
        /* Return if number of expected != number of actual parameters */
        return;
    }

    ssSetNumContStates(S, 0);
    ssSetNumDiscStates(S, 0);

    if (!ssSetNumInputPorts(S, 1)) return;
    ssSetInputPortWidth(S, 0, DYNAMICALLY_SIZED);
    ssSetInputPortRequiredContiguous(S, 0, true); /*direct input signal access*/
    /*
     * Set direct feedthrough flag (1=yes, 0=no).
     * A port has direct feedthrough if the input is used in either
     * the mdlOutputs or mdlGetTimeOfNextVarHit functions.
     */
    ssSetInputPortDirectFeedThrough(S, 0, 1);

    /*7 output signals, all of them scalar*/
    if (!ssSetNumOutputPorts(S, 0)) return;

    ssSetNumSampleTimes(S, 1); //This is extremely important as it may affect the probability of a fault being drawn
    ssSetNumRWork(S, 0);
    ssSetNumIWork(S, 0);
    ssSetNumPWork(S, 0);
    ssSetNumModes(S, 0);
    ssSetNumNonsampledZCs(S, 0);

    ssSetSFcnParamTunable(S,0,false);
    ssSetSFcnParamTunable(S,1,false);
    ssSetSFcnParamTunable(S,2,false);
    ssSetSFcnParamTunable(S,3,false);

    /* Specify the sim state compliance to be same as a built-in block */
    ssSetSimStateCompliance(S, USE_DEFAULT_SIM_STATE);

    ssSetOptions(S, 0);
}



/* Function: mdlInitializeSampleTimes =========================================
 * Abstract:
 *    This function is used to specify the sample time(s) for your
 *    S-function. You must register the same number of sample times as
 *    specified in ssSetNumSampleTimes.
 */
//This is extremely important as it may affect the probability of a fault being drawn
static void mdlInitializeSampleTimes(SimStruct *S)
{
    ssSetSampleTime(S, 0, INHERITED_SAMPLE_TIME);
    ssSetOffsetTime(S, 0, 0.0);

}



#define MDL_INITIALIZE_CONDITIONS   /* Change to #undef to remove function */
#if defined(MDL_INITIALIZE_CONDITIONS)
  /* Function: mdlInitializeConditions ========================================
   * Abstract:
   *    In this function, you should initialize the continuous and discrete
   *    states for your S-function block.  The initial states are placed
   *    in the state vector, ssGetContStates(S) or ssGetRealDiscStates(S).
   *    You can also perform any other initialization activities that your
   *    S-function may require. Note, this routine will be called at the
   *    start of simulation and if it is present in an enabled subsystem
   *    configured to reset states, it will be call when the enabled subsystem
   *    restarts execution to reset the states.
   */
  static void mdlInitializeConditions(SimStruct *S)
  {
    if(initValues(S) != 0)
    {
      ssPrintf("Initialization error\n");
      stopFlag = 1;
      ssSetStopRequested(S, 1);
    }
    ssPrintf("Variables Initialized in saveToDB. Rest will be written to the log.\n");
  }
#endif /* MDL_INITIALIZE_CONDITIONS */



#undef MDL_START  /* Change to #undef to remove function */
#if defined(MDL_START) 
  /* Function: mdlStart =======================================================
   * Abstract:
   *    This function is called once at start of model execution. If you
   *    have states that should be initialized once, this is the place
   *    to do it.
   */
  static void mdlStart(SimStruct *S)
  {
  }
#endif /*  MDL_START */



/* Function: mdlOutputs =======================================================
 * Abstract:
 *    In this function, you compute the outputs of your S-function
 *    block.
 */
static void mdlOutputs(SimStruct *S, int_T tid)
{
    const real_T *signalVector = (const real_T*) ssGetInputPortSignal(S,0);
    double clockTime = 0;
    int sampleTime = 60, writingStatus = 0;
    unsigned long intTime = 0;

    clockTime = signalVector[9];

    intTime = (unsigned long)floor(clockTime);

    if(stopFlag != 1) //Try to write to database only if the stop flag is not raised
    {

      //Take only one sample per sample cycle (minimum sample rate is 1 second due to precision issues)
      if(intTime%sampleTime == 0 && lastSampleTime != intTime)
      {
          lastSampleTime = intTime;
          updateSensorValues(signalVector);
          writingStatus = writeToDB((time_t)intTime);

          if(writingStatus != 0)
          {
            logMsg(logFile, "Error ocurred while writing to the DB. Halting simulation.\n");
            //fprintf(logFile, "%s\n", "Error ocurred while writing to the DB. Halting simulation.\n");
            //fflush(logFile);
            ssSetStopRequested(S, 1); //Stop simulation if writing to the DB is not possible
          }
      }
    }
    else
      ssSetStopRequested(S, 1);
}



#undef MDL_UPDATE  /* Change to #undef to remove function */
#if defined(MDL_UPDATE)
  /* Function: mdlUpdate ======================================================
   * Abstract:
   *    This function is called once for every major integration time step.
   *    Discrete states are typically updated here, but this function is useful
   *    for performing any tasks that should only take place once per
   *    integration step.
   */
  static void mdlUpdate(SimStruct *S, int_T tid)
  {
  }
#endif /* MDL_UPDATE */



#undef MDL_DERIVATIVES  /* Change to #undef to remove function */
#if defined(MDL_DERIVATIVES)
  /* Function: mdlDerivatives =================================================
   * Abstract:
   *    In this function, you compute the S-function block's derivatives.
   *    The derivatives are placed in the derivative vector, ssGetdX(S).
   */
  static void mdlDerivatives(SimStruct *S)
  {
  }
#endif /* MDL_DERIVATIVES */



/* Function: mdlTerminate =====================================================
 * Abstract:
 *    In this function, you should perform any actions that are necessary
 *    at the termination of a simulation.  For example, if memory was
 *    allocated in mdlStart, this is the place to free it.
 */
static void mdlTerminate(SimStruct *S)
{
  if(connectionUp == 1)
  {
    logMsg(logFile, "Attempting to close DB connection");
    mysql_close(con);
    logMsg(logFile, "DB connection closed");
  }
  else
    logMsg(logFile, "No DB connection");
  
  fclose(startDateTimeFile);
  fclose(logFile);
}


/*Function specific functions (implementation)*/

int initValues(SimStruct *S)
{
  int bytesRead = 0, connectionStatus = 0;
  char host[32]={}, user[128]={}, pass[128]={}, db[16]={};

  lastSampleTime = -1; //Initilize to -1 to take the sample at time 0
  stopFlag = 0; //Set stop flag to 0
  sensorValues.controlValue = 0;
  sensorValues.pressureValveInlet = 0;
  sensorValues.pressureValveOutlet = 0;
  sensorValues.rodDisplacement = 0;
  sensorValues.disturbedMediumFlow = 0;
  sensorValues.mediumTemperature = 0;
  sensorValues.faultIntensity = 0;
  sensorValues.selectedFault = 0;
  sensorValues.faultType = 0;

  char msg[128];
  connectionUp = 0;

  logFile = fopen("DamadicsDatabaseLog.txt", "a");

  if(logFile == NULL){
    ssPrintf("Could not open log file for Database\n");
    return -1;
  }

  //sprintf(host, "%s", mxArrayToString(ssGetSFcnParam(S, 0)));
  //logMsg(logFile, host);
  //mxGetString(ssGetSFcnParam(S, 0), host, mxGetM(ssGetSFcnParam(S, 0)) + 1);
  //logMsg(logFile, host);

  mexPrintf("Inside init values");

  //Read connection parameters for the database
  if(mxGetString(ssGetSFcnParam(S, 0), host, mxGetN(ssGetSFcnParam(S, 0))*sizeof(mxChar) + 1) != 0 &&
  mxGetString(ssGetSFcnParam(S, 1), user, mxGetN(ssGetSFcnParam(S, 1))*sizeof(mxChar) + 1) != 0 &&
  mxGetString(ssGetSFcnParam(S, 2), pass, mxGetN(ssGetSFcnParam(S, 2))*sizeof(mxChar) + 1) != 0 &&
  mxGetString(ssGetSFcnParam(S, 3), db, mxGetN(ssGetSFcnParam(S, 3))*sizeof(mxChar) + 1) != 0){
    logMsg(logFile, "Unable to read parameters for database connection\n");
    return -1;
  }

  sprintf(msg, "DB Params: host:%s user:%s pass:%s db:%s", host, user, pass, db);
  logMsg(logFile, msg);

  if((startDateTimeFile = fopen("lastDateTime.txt", "r+")) != NULL)
  {
    bytesRead = fscanf(startDateTimeFile, "%li", &startDateTime);

    if(bytesRead == 0 || bytesRead == EOF)
      startDateTime = time(NULL);
  }
  else
  {
    if((startDateTimeFile = fopen("lastDateTime.txt", "w+")) == NULL)
      return -1;

    startDateTime = time(NULL);
  }

  connectionStatus = connect_to_DB(host, user, pass, db);
  connectionStatus = -1;

  if(connectionStatus == 0)
  {
    sprintf(msg, "Succesfully connected to: %s\n", (char *)mysql_get_client_info());
    logMsg(logFile, msg);
    connectionUp = 1;
    //fprintf(logFile, "Succesfully connected to: %s\n", mysql_get_client_info());
    //fflush(logFile);
  }
  else
  {
    logMsg(logFile, "Connection to the database failed\n");
    //fprintf(logFile, "Connection to the database failed\n");
    //fflush(logFile);
    return -1;
  }

  return 0;
}

int connect_to_DB(char *host, char *user, char *pass, char *db)
{

  con = mysql_init(NULL);
  char msg[350];

  if (con == NULL) 
  {
      sprintf(msg, "%s\n", mysql_error(con));
      logMsg(logFile, msg);
      //fprintf(logFile, "%s\n", mysql_error(con));
      //fflush(logFile);
      return -1;
  }
  sprintf(msg, "Attempting connection to DB with Params: host:%s user:%s pass:%s db:%s", host, user, pass, db);
  logMsg(logFile, msg);
  if (mysql_real_connect(con, host, user, pass, db, 3306, NULL, 0) == NULL) 
  //if (mysql_real_connect(con, "192.168.56.1", "controlslab", "controlslab", "damadics2", 3306, NULL, 0) == NULL) 
  {
      sprintf(msg, "Unable to connect to DB\n");
      //sprintf(msg, "%s\n", mysql_error(con));
      logMsg(logFile, msg);
      //fprintf(logFile, "%s\n", mysql_error(con));
      //fflush(logFile);
      //mysql_close(con);
      return -1;
  }  

  return 0;

}

int writeToDB(time_t elapsedSeconds)
{

  char queryString[500], dateTimeStr[100], msg[128];
  time_t currentSimulationTime = startDateTime + elapsedSeconds;
  struct tm simulationDateTime = *localtime(&currentSimulationTime);

  sprintf(dateTimeStr, "%04d-%02d-%02d %02d:%02d:%02d", simulationDateTime.tm_year + 1900, simulationDateTime.tm_mon + 1, 
    simulationDateTime.tm_mday, simulationDateTime.tm_hour, simulationDateTime.tm_min, simulationDateTime.tm_sec);

  sprintf(queryString, "INSERT INTO valveReadings(timestamp, externalControllerOutput, disturbedMediumFlow,\
    pressureValveInlet, pressureValveOutlet, mediumTemperature, rodDisplacement, selectedFault, faultType, faultIntensity)\
    VALUES ('%s', %f, %f, %f, %f, %f, %f, %d, %d, %f)", dateTimeStr, sensorValues.controlValue, sensorValues.disturbedMediumFlow, 
    sensorValues.pressureValveInlet, sensorValues.pressureValveOutlet, sensorValues.mediumTemperature, sensorValues.rodDisplacement, 
    sensorValues.selectedFault, sensorValues.faultType, sensorValues.faultIntensity);

  //fprintf(stdout, "%s\n", queryString);

  if (mysql_query(con, queryString))
    {
      sprintf(msg, "%s\n", mysql_error(con));
      logMsg(logFile, msg);
      //fprintf(logFile, "%s\n", mysql_error(con));
      //fflush(logFile);
      return -1;
    }
    else
    {
      //fprintf(logFile, "Writing to DB at: %s\n", dateTimeStr);
      fseek(startDateTimeFile, 0, SEEK_SET);
      fprintf(startDateTimeFile, "%li\n", currentSimulationTime+1);
    }

    return 0;
}

void updateSensorValues(const real_T *signalVector)
{
  sensorValues.controlValue = (double)signalVector[0];
  sensorValues.pressureValveInlet = (double)signalVector[1];
  sensorValues.pressureValveOutlet = (double)signalVector[2];
  sensorValues.rodDisplacement = (double)signalVector[3];
  sensorValues.disturbedMediumFlow = (double)signalVector[4];
  sensorValues.mediumTemperature = (double)signalVector[5];
  sensorValues.faultIntensity = (double)signalVector[6];
  sensorValues.selectedFault = (int)signalVector[7];
  sensorValues.faultType = (int)signalVector[8];
}

/*=============================*
 * Required S-function trailer *
 *=============================*/

#ifdef  MATLAB_MEX_FILE    /* Is this file being compiled as a MEX-file? */
#include "simulink.c"      /* MEX-file interface mechanism */
#else
#include "cg_sfun.h"       /* Code generation registration function */
#endif
