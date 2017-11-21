#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <mysql.h>

int connect_to_DB(void);
int savetoDB(time_t);

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
FILE *startDateTimeFile;

int main(int argc, char **argv)
{

	int connectionStatus = 0, sampleTime = 60;
	time_t currentTime = time(NULL); //Current time
	time_t intTime = 0, fracTime = 0;

	intTime = floor(currentTime);
	fracTime = currentTime - intTime;

	connectionStatus = connect_to_DB();

	if(connectionStatus == 0)
	{
  		printf("MySQL client version: %s\n", mysql_get_client_info());

  		//Write samples to the database
		if(fracTime == 0 && intTime%sampleTime == 0 && alreadySampled == 0)
		{
			alreadySampled = 1;
			writeToDB(currentTime);
		}
		else if(alreadySampled == 1 && intTime%sampleTime != 0)
    		alreadySampled = 0;
	}
  	else
  		printf("Connection failed");

  	mysql_close(con);

  	return 0;
}

void initValues(void)
{
	alreadySampled = 0;
	sensorValues.controlValue = 0;
	sensorValues.pressureValveInlet = 0;
	sensorValues.pressureValveOutlet = 0;
	sensorValues.rodDisplacement = 0;
	sensorValues.disturbedMediumFlow = 0;
	sensorValues.mediumTemperature = 0;
	sensorValues.faultIntensity = 0;
	sensorValues.selectedFault = 0;
	sensorValues.faultType = 0;
	connect_to_DB();
}

int connect_to_DB(void)
{

  con = mysql_init(NULL);

  if (con == NULL) 
  {
      fprintf(stdout, "%s\n", mysql_error(con));
      return -1;
  }

  if (mysql_real_connect(con, "localhost", "dlaredorazo", "@Dexsys13", "damadics", 3306, NULL, 0) == NULL) 
  {
      fprintf(stdout, "%s\n", mysql_error(con));
      mysql_close(con);
      return -1;
  }  

  return 0;

}

int writeToDB(time_t currentTime)
{

	char queryString[500], dateTimeStr[100];
	struct tm dateTime = *localtime(&currentTime);

	sprintf(dateTimeStr, "%04d-%02d-%02d %02d:%02d:%02d", dateTime.tm_year + 1900, dateTime.tm_mon + 1, dateTime.tm_mday, 
			dateTime.tm_hour, dateTime.tm_min, dateTime.tm_sec);

	sprintf(queryString, "INSERT INTO valveReadings(timestamp, externalControllerOutput, disturbedMediumFlow,\
		pressureValveInlet, pressureValveOutlet, mediumTemperature, rodDisplacement, selectedFault, faultType, faultIntensity)\
		VALUES ('%s', %f, %f, %f, %f, %f, %f, %d, %d, %f)", dateTimeStr, sensorValues.controlValue, sensorValues.disturbedMediumFlow, 
		sensorValues.pressureValveInlet, sensorValues.pressureValveOutlet, sensorValues.mediumTemperature, sensorValues.rodDisplacement, 
		sensorValues.selectedFault, sensorValues.faultType, sensorValues.faultIntensity);

	printf("%s\n", queryString);

	/*
	if (mysql_query(con, queryString))
  	{
      fprintf(stdout, "%s\n", mysql_error(con));
      return -1;
  	}*/

  	return 0;
}




