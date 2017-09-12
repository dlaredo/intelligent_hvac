import zeep
import traceback
import sqlalchemy
import math
import time
import threading
import logging
from zeep.transports import Transport
from requests.auth import HTTPBasicAuth
from requests import Session as WebSession
from datetime import datetime, timezone, timedelta
from hvacDBMapping import *
from sqlalchemy.orm import sessionmaker
from queue import Queue
from threading import Thread

global componentsList, componentsClasses, readings, trendServiceClient, startDateTime, endDateTime

componentsList = ["AHU", "VFD", "Filter", "Damper", "Fan", "HEC", "SAV", "VAV", "Thermafuser"]
componentsClasses = {"ahu":AHU, "vfd":VFD, "filter":Filter, "damper":Damper, "fan":Fan, "hec":HEC, "sav":SAV, "vav":VAV, "thermafuser":Thermafuser}
readingClasses = {"ahu":AHUReading, "vfd":VFDReading, "filter":FilterReading, "damper":DamperReading, "fan":FanReading, "hec":HECReading, "sav":SAVReading, "vav":VAVReading, "thermafuser":ThermafuserReading}

class PullingWorker(Thread):
	"""multithreaded worker to pull data from the data sourcer (ALC)"""

	global readings, trendServiceClient, startDateTime, endDateTime

	def __init__(self, queue, lock, key, tname):
		Thread.__init__(self, name=tname)
		self.queue = queue
		self.key = key
		self.lock = lock
		self.maxTimesRead = 5

	def run(self):

		#print("Thread started " + threading.current_thread().getName())

		while self.queue.empty() == False:

			# Get the work from the queue and expand the tuple
			data = self.queue.get()

			dataPoint, timesRead = data
			path, componentId, databaseMapping = dataPoint

			reading = readings[componentId]

			#Attempt to get the data from the server
			try:
				data = trendServiceClient.service.getTrendData('soap',"", path, startDateTime.strftime("%m/%d/20%y %I:%M:%S %p"), endDateTime.strftime("%m/%d/20%y %I:%M:%S %p"), False, 0)

				#If the reading returned some values, store them
				if len(data) != 0:
					readingValue = data[-1]
					#print(path, readingValue)
					setattr(reading, databaseMapping, readingValue)
				#If the webservice returned and empty array and the maximum number of attempts hasnt been reached insert the path in the queue to attempt reading again.
				elif timesRead > self.maxTimesRead:
					queue.put((dataPoint, timesRead+1))
				else:   #After maxTimesRead attempts, insert None as the data since it could not be read.
					setattr(reading, databaseMapping, None)
					print("Empty value for " + path + " after " + str(self.maxTimesRead) + " attempts")
					logging.error("Empty value for " + path + " after " + str(self.maxTimesRead) + " attempts")
			except Exception as e:
				setattr(reading, databaseMapping, None)
				#lock.acquire()
				print("Error in retrieving value for " + path)
				logging.error("Error in retrieving value for " + path)
				logging.error(traceback.format_exc())
				#lock.release()
			finally:
				self.queue.task_done()

		#print("Thread exit " + threading.current_thread().getName())


def createReadingClasses(dataPoints, endDateTime, key):
	"""Create the necessary reading classes to store the readings"""

	global readings

	readings = dict()

	for dataPoint in dataPoints[key]:
		path, componentId, databaseMapping = dataPoint

		if componentId not in readings:
			readingClass = readingClasses[key](endDateTime, componentId)
			readings[componentId] = readingClass


def getClient(servicewsdl):
	"""Attempt to stablish a connection to the webservice and return a client object connected to servicewsdl webservice"""

	client = None

	try:
		webSession = WebSession()
		webSession.auth = HTTPBasicAuth('soap', "")
		transport = Transport(timeout=10, session = webSession)
		client = zeep.Client(wsdl=servicewsdl, transport=transport)
		print('Client successfully created')
		logging.info('Client successfully created')
	except Exception as e:
		print("Error in getting a client to the webservice")
		logging.critical("Error in getting a client to the webservice")
		logging.critical(traceback.format_exc())

	return client


def getDatabaseConnection(databaseString):
	"""Attempt connection to the database"""
	
	sqlsession = None

	try:
		sqlengine = sqlalchemy.create_engine(databaseString)
		SQLSession = sessionmaker(bind=sqlengine)
		sqlsession = SQLSession()

		print("Connection to " + databaseString + " successfull")
		logging.info("Connection to " + databaseString + " successfull")
	except Exception as e:
		logging.error("Error in connection to the database")
		logging.error(traceback.format_exc())
		print("Error in connection to the database")

	return sqlsession


def pullData_multiThread(databaseSession, finishingDateTime=None):
	"""Retrieve the data stored in the trend points of the WebCtrl program from the indicated startDateTime onwards and store them in the database.
	This function will pull data from the database every 5 minutes starting from startDateTime and will keep doing it indefinetly."""

	global readings, startDateTime, endDateTime

	numberOfThreads = 20

	#get the datapoints and separate them by component type (this should be relaunched everytime the database is modified)
	dataPoints = {key.lower():databaseSession.query(DataPoint._path, DataPoint._componentId, PathMapping._databaseMapping).
	join(PathMapping).filter(PathMapping._componentType == key).all() for key in componentsList}

	PDT = timezone(-timedelta(hours=7), 'PDT')
	timeDelta = timedelta(minutes = 5)

	lock = threading.Lock()

	if finishingDateTime != None:
		continueUntil = lambda endingDateTime : endingDateTime <= finishingDateTime
		print("Finishing dateTime " + str(finishingDateTime))
		logging.info("Finishing dateTime " + str(finishingDateTime))
	else:
		continueUntil = lambda endingDateTime : True

	endDateTime = startDateTime + timeDelta
	#If a finishing datetime is defined continue until that datetime is reached, otherwise continue indefinetely
	while continueUntil(endDateTime):

		currentTime = datetime.now(tz=PDT)
		currentTime = currentTime.replace(second=0, microsecond=0)

		print("Pulling data from " + str(startDateTime) + " to " + str(endDateTime))
		logging.info("Pulling data from " + str(startDateTime) + " to " + str(endDateTime))

		#If desired time hasnt been reached yet, wait until it has been reached
		if currentTime < endDateTime:
			waitingMinutes = (endDateTime - currentTime) + timedelta(minutes=1)
			print(str(currentTime) + " Desired time " + str(endDateTime) + " not reached yet, halting for " + str(waitingMinutes) + " minutes")
			logging.info(str(currentTime) + " Desired time " + str(endDateTime) + " not reached yet, halting for " + str(waitingMinutes) + " minutes")
			time.sleep(waitingMinutes.seconds)
			print("Desired time reached, continuing job")
			logging.info("Desired time reached, continuing job")

		#For each type of components get its readings from the web service
		for key in dataPoints:
			
			print("\nPulling points of " + key + "\n")
			logging.info("\nPulling points of " + key + "\n")

			#create the necessary classes for the readings
			createReadingClasses(dataPoints, endDateTime, key)

			# Create a queue to communicate with the worker threads
			queue = Queue()

			#Add datapoints to the queue
			for dataPoint in dataPoints[key]:
				queue.put((dataPoint, 1))
			
			#create the threads and start them
			# Create 8 worker threads
			workingThreads  = list()
			for i in range(numberOfThreads):
				workingThreads.append(PullingWorker(queue, lock, key, 'Thread-' + str(i+1)))
				workingThreads[i].start()

			#Wait until all of the threads have finished
			queue.join()
			for i in range(numberOfThreads):
				workingThreads[i].join()
			
			databaseSession.add_all(readings.values())

		databaseSession.commit()
		print("Readings stored in the Database")
		logging.info("Readings stored in the Database")

		#Define the new start time and end time
		startDateTime = endDateTime
		endDateTime = startDateTime + timeDelta

		#Exit loop
		#break


def main():


	global trendServiceClient, startDateTime

	Evalwsdl = 'http://10.20.0.47/_common/webservices/Eval?wsdl'
	Trendwsdl = 'http://10.20.0.47/_common/webservices/TrendService?wsdl'

	databaseString = "mysql+mysqldb://controlslab:controlslab@localhost:3306/HVACInternetTest"

	#set the logger config
	logging.basicConfig(filename='dataPull.log', level=logging.INFO,\
	format='%(levelname)s:%(threadName)s:%(asctime)s:%(filename)s:%(funcName)s:%(message)s', datefmt='%m/%d/%Y %H:%M:%S')

	#Make sure starting time is a multiple of 5 in the minutes and that its a past time.
	#To ensure that we will be able to get the readings we try to get the readings from 5+ minutes before the current time. 
	PDT = timezone(-timedelta(hours=7), 'PDT')
	startDateTime = datetime.now(tz=PDT)
	minute = math.floor(startDateTime.minute/5)*5 - 5
	
	if minute < 0:
		minute = 55
		differenceInHours = startDateTime - timedelta(hours=1)
		startDateTime = startDateTime.replace(second=0, microsecond=0, minute=minute, hour=differenceInHours.hour)
	else:
		startDateTime = startDateTime.replace(second=0, microsecond=0, minute=minute)

	#override start Datetime and finish Datetime to specify another starting dateTime
	startDateTime = datetime(2017, 9, 10, hour=13, minute=55, second=0, microsecond=0, tzinfo=PDT)
	finishingDateTime = datetime(2017, 9, 10, hour=14, minute=0, second=0, microsecond=0, tzinfo=PDT)
	
	print("Start time " + str(startDateTime))

	#get a connection to the webservice
	trendServiceClient = getClient(Trendwsdl)
	sqlsession = getDatabaseConnection(databaseString)

	if trendServiceClient != None and sqlsession != None:
		#pullData_multiThread(sqlsession)
		pullData_multiThread(sqlsession, finishingDateTime)

	print("Main exit")


main()