import zeep
import traceback
import sqlalchemy
import math
import time
from zeep.transports import Transport
from requests.auth import HTTPBasicAuth
from requests import Session as WebSession
from datetime import datetime, timezone, timedelta
from hvacDBMapping import *
from sqlalchemy.orm import sessionmaker

global componentsList, componentsClasses
componentsList = ["AHU", "VFD", "Filter", "Damper", "Fan", "HEC", "SAV", "VAV", "Thermafuser"]
componentsClasses = {"ahu":AHU, "vfd":VFD, "filter":Filter, "damper":Damper, "fan":Fan, "hec":HEC, "sav":SAV, "vav":VAV, "thermafuser":Thermafuser}
readingClasses = {"ahu":AHUReading, "vfd":VFDReading, "filter":FilterReading, "damper":DamperReading, "fan":FanReading, "hec":HECReading, "sav":SAVReading, "vav":VAVReading, "thermafuser":ThermafuserReading}

def getClient(servicewsdl):
	"""Attempt to stablish a connection to the webservice and return a client object connected to servicewsdl webservice"""

	client = None

	try:
		webSession = WebSession()
		webSession.auth = HTTPBasicAuth('soap', "")
		transport = Transport(timeout=10, session = webSession)
		client = zeep.Client(wsdl=servicewsdl, transport=transport)
		print('Client successfully created')
	except Exception as e:
		print(traceback.format_exc())
		print("error in getting a client to the webservice")

	return client


def getDatabaseConnection(databaseString):
	"""Attempt connection to the database"""
	
	sqlsession = None

	try:
		sqlengine = sqlalchemy.create_engine(databaseString)
		SQLSession = sessionmaker(bind=sqlengine)
		sqlsession = SQLSession()

		print("Connection to " + databaseString + " successfull")
	except Exception as e:
		print(traceback.format_exc())
		print("Error in connection to the database")

	return sqlsession


def pullData(trendServiceClient, startDateTime, databaseSession):
	"""Retrieve the data stored in the trend points of the WebCtrl program from the indicated startDateTime onwards and store them in the database.
	This function will pull data from the database every 5 minutes starting from startDateTime and will keep doing it indefinetly."""

	#get the datapoints and separate them by component type (this should be relaunched everytime the database is modified)
	dataPoints = {key.lower():databaseSession.query(DataPoint._path, DataPoint._componentId, PathMapping._databaseMapping).
	join(PathMapping).filter(PathMapping._componentType == key).all() for key in componentsList}

	PDT = timezone(-timedelta(hours=7), 'PDT')
	timeDelta = timedelta(minutes = 5)

	#Repeat indefinetely
	while True:

		#Define the endTime
		endDateTime = startDateTime + timeDelta
		currentTime = datetime.now(tz=PDT)
		currentTime = currentTime.replace(second=0, microsecond=0)

		#If desired time hasnt been reached yet, wait for a couple of minutes
		if currentTime < endDateTime:
			waitingMinutes = (endDateTime - currentTime) + timedelta(minutes=1)
			print(str(currentTime) + " Desired time " + str(endDateTime) + " not reached yet, halting for " + str(waitingMinutes) + " minutes")
			time.sleep(waitingMinutes.seconds)
			print("Desired time reached, continuing job")

		#For each type of components get its readings from the web service
		for key in dataPoints:
			
			print("\nPulling points of " + key + "\n")
			components = dict()
			
			for dataPoint in dataPoints[key]:
				path, componentId, databaseMapping = dataPoint

				if componentId in components:
					component = components[componentId]
				else:
					component = readingClasses[key](endDateTime, componentId)
					components[componentId] = component

				try:
					data = trendServiceClient.service.getTrendData('soap',"", path, startDateTime.strftime("%m/%d/20%y %I:%M:%S %p"), endDateTime.strftime("%m/%d/20%y %I:%M:%S %p"), False, 0)
					
					#Check if the current point already has a component
					readingValue = data[-1]
					print(path, readingValue)
					setattr(component, databaseMapping, readingValue)
				except Exception as e:
					print(traceback.format_exc())
					print("Error in retrieving value for " + path)

			databaseSession.add_all(components.values())

		databaseSession.commit()

		#Define the new start time
		startDateTime = endDateTime

		break

def main():


	Evalwsdl = 'http://10.20.0.47/_common/webservices/Eval?wsdl'
	Trendwsdl = 'http://10.20.0.47/_common/webservices/TrendService?wsdl'

	databaseString = "mysql+mysqldb://dlaredorazo:@Dexsys13@localhost:3306/HVAC2"

	#Make sure starting time is a multiple of 5 in the minutes and that its a past time.
	#To ensure that we will be able to get the readings we try to get the readings from 5+ minutes before the current time. 
	PDT = timezone(-timedelta(hours=7), 'PDT')
	startTime = datetime.now(tz=PDT)
	minute = math.floor(startTime.minute/5)*5 - 5
	
	if minute < 0:
		minute = 55
		hour = startTime - timedelta(hour=1)
		startTime = startTime.replace(second=0, microsecond=0, minute=minute, hour=hour)
	else:
		startTime = startTime.replace(second=0, microsecond=0, minute=minute)
	
	print("Start time " + str(startTime))

	#get a connection to the webservice
	trendServiceClient = getClient(Trendwsdl)
	sqlsession = getDatabaseConnection(databaseString)

	if trendServiceClient != None and sqlsession != None:
		pullData(trendServiceClient, startTime, sqlsession)


main()