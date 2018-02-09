#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int sendMail(char *);
void logMsg(FILE *, char *);
void getCurrentTime(char *);

int sendMail(char *msg){

	char cmd[100];  // to hold the command.
    char to[] = "dlaredorazo@ucmerced.edu"; // email id of the recepient.
    char from[] = "dlaredorazo@gmail.com";
    char subject[] = "Simulation failure";    // email body.
    char tempFile[100];     // name of tempfile.

    strcpy(tempFile,tempnam("/tmp","sendmail")); // generate temp file name.

    FILE *fp = fopen(tempFile,"w"); // open it for writing.

    fprintf(fp, "To: %s\nFrom: %s\nSubject: %s\n\n", to, from, subject);

    fprintf(fp,"%s\n", msg); // write body to it.
    fclose(fp);             // close it.

    sprintf(cmd,"ssmtp %s < %s",to,tempFile); // prepare command.
    system(cmd);     // execute it.

    return 0;

}

void getCurrentTime(char *timeString){

	time_t rawtime;
	struct tm * timeinfo;

	time(&rawtime);
	timeinfo = localtime(&rawtime);

	sprintf(timeString, "%02d/%02d/%04d %02d:%02d:%02d", timeinfo->tm_mon, timeinfo->tm_mday, 
		1900+timeinfo->tm_year, timeinfo->tm_hour, timeinfo->tm_min, timeinfo->tm_sec);
}

void logMsg(FILE *logfile, char *msg){

	char logMsg[512] = {};
	char timeString[128] = {};

	getCurrentTime(timeString);
	strcpy(logMsg, timeString);
	strcat(logMsg, "\t");
	strcat(logMsg, msg);

	fprintf(logfile, "%s\n", logMsg);

}

int main(){

	char ctime[100];
	FILE *fp = NULL;

	fp = fopen("test.txt", "w");

	//getCurrentTime(ctime);
	//sendMail("mensaje de prueba\n");

	printf("%s\n", ctime);

	logMsg(fp, "mensaje de prueba");

	fclose(fp);

}