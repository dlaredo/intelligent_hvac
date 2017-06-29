import csv
import sqlalchemy
from hvacDBMapping import *
from sqlalchemy.orm import sessionmaker
import traceback
import datetime
import re

def zonecsvToDb(filepath, dbsession, zone):
	"""Function used to read from csv files"""

	count = 0

	with open(filepath, 'r') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			#skip the header
			if (count == 0):
				count += 1
				continue
			else:

				#add the datapoints to the DB session
				dataPoint = DataPoint(path = row[6], server = row[0], location = row[1], branch = row[2], subBranch = row[3], controlProgram = row[4], point = row[5], zone = zone)
				dbsession.add(dataPoint)
				#print(dataPoint)

		#commit changes to the database
		dbsession.commit()

def getAHUByAHUNumber(AHUNumber, ahus):

	for ahu in ahus:
		if ahu.AHUNumber == AHUNumber:
			return ahu

	return None

def determineComponentNumber(numberRegex, dataString):
	"""Determine the component number based on the path string"""

	componentNumber = 0
	matchComponentNumber = numberRegex.search(dataString) #Look for the number of the component and create a new component for each new component number found

	if matchComponentNumber:
		componentNumber = int(matchComponentNumber.group())

	return componentNumber

def getStoredAHUComponentsId(stored_ahus):
	"""Return a dictionary containing the component numbers for each of the stored AHUs"""

	ahu_numbers = set()

	fan_numbers = set()
	damper_numbers = set()
	hec_numbers = set()
	filter_numbers = set()

	ahu_fan_numbers = {}
	ahu_damper_numbers = {}
	ahu_hec_numbers = {}
	ahu_filter_numbers = {}

	for ahu in stored_ahus:
		ahu_numbers.add(ahu.AHUNumber)

		for ahu_fan in ahu.fans:
			fan_numbers.add(ahu_fan.fanNumber)

		for ahu_damper in ahu.dampers:
			damper_numbers.add(ahu_damper.damperNumber)

		for ahu_filter in ahu.filters:
			filter_numbers.add(ahu_filter.filterNumber)

		for ahu_hec in ahu.hecs:
			hec_numbers.add(ahu_hec.hecNumber)

		ahu_fan_numbers[ahu.AHUNumber] = fan_numbers
		ahu_damper_numbers[ahu.AHUNumber] = damper_numbers
		ahu_hec_numbers[ahu.AHUNumber] = filter_numbers
		ahu_filter_numbers[ahu.AHUNumber] = hec_numbers

	return ahu_numbers, ahu_fan_numbers, ahu_damper_numbers, ahu_hec_numbers, ahu_filter_numbers

def determineDataPointTypeByPath(path):
	"""Given the path of the datapoint determine its type"""

	if "ahu" in path or "AHU" in path:
		return "AHU"
	if "vav" in path or "VAV" in path:
		return "VAV"
	if "sav" in path or "SAV" in path:
		return "SAV"
	if "thermafuser" in path or "Thermafuser" in path or "THERMAFUSER" in path:
		return "Thermafuser"

	return None

def StoreAHUDataPoints(session):
	"""Store all the data points corresponding to AHUs"""

	#get all data points
	datapoints = session.query(DataPoint).all()

	for dataPoint in datapoints:

		splittedPath = dataPoint.path.split("/")
		componentPath = splittedPath[len(splittedPath) - 1]
		#print(componentPath)
		mappedDataPoint = session.query(PathMapping).filter(PathMapping._path == componentPath).first()

		if mappedDataPoint == None:
			#If datapoint doesnt exactly match

			mappedDataPoints = session.query(PathMapping).filter(PathMapping._path.like('%'+componentPath+'%')).all()

			#print(dataPoint.path)

			if len(mappedDataPoints) > 0:

				for mappedDataPoint in mappedDataPoints:
					dataPointType = determineDataPointTypeByPath(dataPoint.path)
					print(dataPointType)

					if dataPointType == mappedDataPoint.componentType:
						#We know to what the point maps to
						break

			else:
				print(dataPoint.path + " mapped data point not found")
		else:
			#print(mappedDataPoint.componentType)
			if mappedDataPoint.componentType == "AHU":
				#We know to what the point maps to
				pass
				#print(dataPoint.path)
				#print(mappedDataPoint.databaseMapping)

	session.close()


def main():
	"""Main function"""

	zone4FilepATH = "../csv_files/Zone4.csv"
	
	#Attempt connection to the database
	try:
		sqlengine = sqlalchemy.create_engine("mysql+mysqldb://dlaredorazo:@Dexsys13@localhost:3306/HVAC")
		Session = sessionmaker(bind=sqlengine)
		session = Session()

		print("Connection successfull")
	except Exception as e:
		print(traceback.format.exc())
		print("Error in connection")
		return False

	#Attempt to write csv to the database
	#zonecsvToDb(zone4FilepATH, session, "4")
	print("writting sucessfull")

	StoreAHUDataPoints(session)



#invoke main
main()




