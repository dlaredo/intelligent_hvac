/*
 * sfuntmpl_basic.c: Basic 'C' template for a level 2 S-function.
 *
 * Copyright 1990-2013 The MathWorks, Inc.
 */


/*
 * You must specify the S_FUNCTION_NAME as the name of your S-function
 * (i.e. replace sfuntmpl_basic with the name of your S-function).
 */

#define S_FUNCTION_NAME  saveToDB2
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
#include "utils.h"

#define INPUT_PARAMS 1

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

    /* Specify the sim state compliance to be same as a built-in block */
    ssSetSimStateCompliance(S, USE_DEFAULT_SIM_STATE);

    ssSetOptions(S, SS_OPTION_CALL_TERMINATE_ON_EXIT);
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

  mexPrintf("DB Params: host:%d\n", mxGetN(ssGetSFcnParam(S, 0))*sizeof(mxChar) + 1);

  //Read connection parameters for the database
  if(mxGetString(ssGetSFcnParam(S, 0), host, mxGetN(ssGetSFcnParam(S, 0))*sizeof(mxChar) + 1) != 0)
  {
    logMsg(logFile, "Unable to read parameters for database connection\n");
    return -1;
  }

  mexPrintf("DB Params: host:%s\n", host);
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