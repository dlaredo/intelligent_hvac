import zeep
import traceback
import sqlalchemy
import math
import time
import threading
from zeep.transports import Transport
from requests.auth import HTTPBasicAuth
from requests import Session as WebSession
from datetime import datetime, timezone, timedelta
from hvacDBMapping import *
from sqlalchemy.orm import sessionmaker
from queue import Queue
from threading import Thread

global componentsList, componentsClasses, components, trendServiceClient, startDateTime, endDateTime

componentsList = ["AHU", "VFD", "Filter", "Damper", "Fan", "HEC", "SAV", "VAV", "Thermafuser"]
componentsClasses = {"ahu":AHU, "vfd":VFD, "filter":Filter, "damper":Damper, "fan":Fan, "hec":HEC, "sav":SAV, "vav":VAV, "thermafuser":Thermafuser}
readingClasses = {"ahu":AHUReading, "vfd":VFDReading, "filter":FilterReading, "damper":DamperReading, "fan":FanReading, "hec":HECReading, "sav":SAVReading, "vav":VAVReading, "thermafuser":ThermafuserReading}

class PullingWorker(Thread):
	"""multithreaded worker to pull data from the data sourcer (ALC)"""

	global components, trendServiceClient, startDateTime, endDateTime

	def __init__(self, queue, lock, key):
		Thread.__init__(self)
		self.queue = queue
		self.lock = lock
		self.key = key

	def run(self):

		while True:
			# Get the work from the queue and expand the tuple
			dataPoint = self.queue.get()

			#If the queue is empty
			if dataPoint is None:
				break

			path, componentId, databaseMapping = dataPoint

			#lock the threads so that the components are added properly
			self.lock.acquire()
			if componentId in components:
				component = components[componentId]
			else:
				component = readingClasses[self.key](endDateTime, componentId)
				components[componentId] = component
			self.lock.release()

			#Attempt to get the data from the server and create the object
			try:
				data = trendServiceClient.service.getTrendData('soap',"", path, startDateTime.strftime("%m/%d/20%y %I:%M:%S %p"), endDateTime.strftime("%m/%d/20%y %I:%M:%S %p"), False, 0)

				#Check if the current point already has a component
				readingValue = data[-1]
				#print(path, readingValue)
				setattr(component, databaseMapping, readingValue)
			except Exception as e:
				print("Error in retrieving value for " + path)
				logging.error("Error in retrieving value for " + path)
				logging.error(traceback.format_exc())
				setattr(component, databaseMapping, None)

			self.queue.task_done()


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
		logging.info("Connection to " + database + " successfull")
	except Exception as e:
		logging.error("Error in connection to the database")
		logging.error(traceback.format_exc())
		print("Error in connection to the database")

	return sqlsession


def pullData_multiThread(databaseSession):
	"""Retrieve the data stored in the trend points of the WebCtrl program from the indicated startDateTime onwards and store them in the database.
	This function will pull data from the database every 5 minutes starting from startDateTime and will keep doing it indefinetly."""

	global components, startDateTime, endDateTime

	#get the datapoints and separate them by component type (this should be relaunched everytime the database is modified)
	dataPoints = {key.lower():databaseSession.query(DataPoint._path, DataPoint._componentId, PathMapping._databaseMapping).
	join(PathMapping).filter(PathMapping._componentType == key).all() for key in componentsList}

	PDT = timezone(-timedelta(hours=7), 'PDT')
	timeDelta = timedelta(minutes = 5)

	lock = threading.Lock()

	#Repeat indefinetely
	while True:

		#Define the endTime
		endDateTime = startDateTime + timeDelta
		currentTime = datetime.now(tz=PDT)
		currentTime = currentTime.replace(second=0, microsecond=0)

		print("Pulling data from " + str(startDateTime) + " to " + str(endDateTime))
		logging.info("Pulling data from " + str(startDateTime) + " to " + str(endDateTime))

		#If desired time hasnt been reached yet, wait for a couple of minutes
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
			components = dict()

			# Create a queue to communicate with the worker threads
			queue = Queue()

			#Add datapoints to the queue
			for dataPoint in dataPoints[key]:
				queue.put(dataPoint)
			
			#create the threads and start them
			# Create 8 worker threads
			for x in range(8):
				worker = PullingWorker(queue, lock, key)
				# Setting daemon to True will let the main thread exit even though the workers are blocking
				#worker.daemon = True
				worker.start()

			#Wait until all the threads have finished
			queue.join()
			databaseSession.add_all(components.values())
			#print(components.values())

		databaseSession.commit()

		#Define the new start time
		startDateTime = endDateTime


def main():


	global trendServiceClient, startDateTime

	Evalwsdl = 'http://10.20.0.47/_common/webservices/Eval?wsdl'
	Trendwsdl = 'http://10.20.0.47/_common/webservices/TrendService?wsdl'

	databaseString = "mysql+mysqldb://dlaredorazo:@Dexsys13@localhost:3306/HVAC2"

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
	
	print("Start time " + str(startDateTime))

	#get a connection to the webservice
	trendServiceClient = getClient(Trendwsdl)
	sqlsession = getDatabaseConnection(databaseString)

	if trendServiceClient != None and sqlsession != None:
		pullData_multiThread(sqlsession)


main()