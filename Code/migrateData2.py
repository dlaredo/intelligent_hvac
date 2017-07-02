import csv
import sqlalchemy
from hvacDBMapping import *
from sqlalchemy.orm import sessionmaker
import traceback
import datetime
import re


global numberRegex
numberRegex = re.compile(r'\d+', flags = re.IGNORECASE)

def zonecsvToDb(filepath, dbsession, zone):
	"""Function used to read from csv files"""

	count = 0

	dataPoints = dbsession.query(DataPoint).all()
	dataPointInserted = set()

	for dataPoint in dataPoints:
		dataPointInserted.add(dataPoint.path)

	with open(filepath, 'r') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			#skip the header
			if (count == 0):
				count += 1
				continue
			else:

				path = row[6]
				if path not in dataPointInserted:
					#add the datapoints to the DB session
					dataPoint = DataPoint(path = path, server = row[0], location = row[1], branch = row[2], subBranch = row[3], controlProgram = row[4], point = row[5], zone = zone)
					dbsession.add(dataPoint)
					#print("writting ", dataPoint)

		#commit changes to the database
		dbsession.commit()

def getAHUByAHUNumber(AHUNumber, ahus):
	"""Get AHU by Ahu Number"""

	for ahu in ahus:
		if ahu.AHUNumber == AHUNumber:
			return ahu

	return None

def determineComponentNumber(pathString):
	"""Determine the component number based on the path string"""

	componentNumber = 0
	matchComponentNumber = numberRegex.findall(pathString.split("/")[0])

	if matchComponentNumber:
		componentNumber = "-".join(matchComponentNumber)

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

def MapDataPoints(session):
	"""Map each datapoint to its corresponding table and component"""

	dataPointMapped = True

	#data structures
	mappedDataPoints = dict()
	mappedDataPoints["ahu"] = list()
	mappedDataPoints["vfd"] = list()
	mappedDataPoints["fan"] = list()
	mappedDataPoints["filter"] = list()
	mappedDataPoints["damper"] = list()
	mappedDataPoints["hec"] = list()
	mappedDataPoints["thermafuser"] = list()
	mappedDataPoints["vav"] = list()
	mappedDataPoints["sav"] = list()

	#get all data points
	datapoints = session.query(DataPoint).all()

	for dataPoint in datapoints:

		#If the point has already been mapped, skip it
		if dataPoint.pathMapping != None:
			mappedDataPoints[dataPoint.pathMapping.componentType.lower()].append(dataPoint)
			continue

		splittedPath = dataPoint.path.split("/")
		componentPath = splittedPath[len(splittedPath) - 1]

		#The datapoint may be a supply/return fan point
		if "rf" in componentPath or "sf" in componentPath:
			fanNumber = determineComponentNumber(componentPath)
			if fanNumber != 0:
				fanSplitted = componentPath.split(str(fanNumber))
				componentPath = fanSplitted[0] + fanSplitted[1]

		mappedDataPoint = session.query(PathMapping).filter(PathMapping._path == componentPath).first()

		#If datapoint doesnt exactly match
		if mappedDataPoint == None:

			mDataPoints = session.query(PathMapping).filter(PathMapping._path.like('%'+componentPath+'%')).all()

			if len(mDataPoints) > 0:

				dataPointType = determineDataPointTypeByPath(dataPoint.path)

				for mDataPoint in mDataPoints:

					if dataPointType == mDataPoint.componentType:
						mappedDataPoint = mDataPoint
						dataPointMapped = True
						break
					else:
						dataPointMapped = False

			else:
				dataPointMapped = False

		if dataPointMapped == False:
			print(dataPoint.path + " DataPoint could not be mapped")		
		else:
			#print(dataPoint.path, dataPoint.controlProgram, mappedDataPoint.databaseMapping)

			dataPoint.pathMappingId = mappedDataPoint.id
			dataPoint.pathMapping = mappedDataPoint
			mappedDataPoint.dataPoints.append(dataPoint)

			mappedDataPoints[mappedDataPoint.componentType.lower()].append(dataPoint)

			session.add(mappedDataPoint)
			session.add(dataPoint)

	session.commit()

	return mappedDataPoints

def printMappedDataPoints(mappedDataPoints):
	"""Print all the mapped datapoints"""

	totalDataPoints = 0
	#print(mappedDataPoints)

	for key in mappedDataPoints:

		componentDataPoints = len(mappedDataPoints[key])
		totalDataPoints += componentDataPoints

		print("\n" + key + " datapoints = ", componentDataPoints)

		for mappedDataPoint in mappedDataPoints[key]:
			print(mappedDataPoint.path, mappedDataPoint.controlProgram, mappedDataPoint.pathMapping.databaseMapping)

	print("\nTotal data points = ", totalDataPoints)


def createListOfNewComponents(ComponentClass, mappedDataPoints, componentKey, componentNumbersList):
	"""Fill components in a list to be inserted to the database"""

	new_components = list()

	for mdataPoint in mappedDataPoints[componentKey]:

		dataPoint = mdataPoint[0]
		mappedDataPoint = mdataPoint[1]

		componentNumber = determineComponentNumber(dataPoint.path)
		print(componentNumber)
		if componentNumber not in componentNumbersList:
			new_components.append(ComponentClass(componentNumber))
			componentNumbersList.add(componentNumber)

	return new_components


def fillComponentsInDatabase(mappedDataPoints, session):
	"""Take the mapped datapoints and fill the corresponding components in the database"""

	#data structures
	#ahu = set()

	#ahus = session.query(AHU).all()

	#for ahu in ahus:
	#	ahuNumbers.add(ahu.AHUNumber)

	#print(ahuNumbers)

	#new_ahus = createListOfNewComponents(AHU, mappedDataPoints, "ahu", ahuNumbers)

	#for new_ahu in new_ahus:
	#	print("AHU " + str(new_ahu.AHUNumber))

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
	try:
		zonecsvToDb(zone4FilepATH, session, "4")
		print("writting sucessfull")
	except:
		print("Error writting to the database")

	print("Mapping DataPoints")
	mappedDataPoints = MapDataPoints(session)

	printMappedDataPoints(mappedDataPoints)

	print("Filling components in Database")
	fillComponentsInDatabase(mappedDataPoints, session)

	session.close()



#invoke main
main()




