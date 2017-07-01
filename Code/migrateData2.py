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

def MapDataPoints(session):
	"""Map each datapoint to its corresponding table and component"""

	dataPointMapped = True

	#data structures
	ahuDataPoints = list()
	vfdDataPoints = list()
	fanDataPoints = list()
	damperDataPoints = list()
	filterDataPoints = list()
	savDataPoints = list()
	vavDataPoints = list()
	hecDataPoints = list()
	thermafuserDataPoints = list()
	mappedDataPoints = dict()

	numberRegex = re.compile(r'\d+', flags = re.IGNORECASE)

	#get all data points
	datapoints = session.query(DataPoint).all()

	for dataPoint in datapoints:

		splittedPath = dataPoint.path.split("/")
		componentPath = splittedPath[len(splittedPath) - 1]

		#The datapoint may be a supply/return fan point
		if "rf" in componentPath or "sf" in componentPath:
			fanNumber = determineComponentNumber(numberRegex, componentPath)
			if fanNumber != 0:
				fanSplitted = componentPath.split(str(fanNumber))
				componentPath = fanSplitted[0] + fanSplitted[1]

		mappedDataPoint = session.query(PathMapping).filter(PathMapping._path == componentPath).first()

		#If datapoint doesnt exactly match
		if mappedDataPoint == None:

			mDataPoints = session.query(PathMapping).filter(PathMapping._path.like('%'+componentPath+'%')).all()

			if len(mDataPoints) > 0:

				for mDataPoint in mDataPoints:
					dataPointType = determineDataPointTypeByPath(dataPoint.path)

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

			if mappedDataPoint.componentType == "AHU":
				ahuDataPoints.append((dataPoint.controlProgram, mappedDataPoint))
			if mappedDataPoint.componentType == "VFD":
				vfdDataPoints.append((dataPoint.controlProgram, mappedDataPoint))
			if mappedDataPoint.componentType == "Fan":
				fanDataPoints.append((dataPoint.controlProgram, mappedDataPoint))
			if mappedDataPoint.componentType == "Filter":
				filterDataPoints.append((dataPoint.controlProgram, mappedDataPoint))
			if mappedDataPoint.componentType == "Damper":
				damperDataPoints.append((dataPoint.controlProgram, mappedDataPoint))
			if mappedDataPoint.componentType == "HEC":
				hecDataPoints.append((dataPoint.controlProgram, mappedDataPoint))
			if mappedDataPoint.componentType == "Thermafuser":
				thermafuserDataPoints.append((dataPoint.controlProgram, mappedDataPoint))
			if mappedDataPoint.componentType == "VAV":
				vavDataPoints.append((dataPoint.controlProgram, mappedDataPoint))
			if mappedDataPoint.componentType == "SAV":
				savDataPoints.append((dataPoint.controlProgram, mappedDataPoint))

	mappedDataPoints["ahu"] = ahuDataPoints
	mappedDataPoints["vfd"] = vfdDataPoints
	mappedDataPoints["fan"] = fanDataPoints
	mappedDataPoints["filter"] = filterDataPoints
	mappedDataPoints["damper"] = damperDataPoints
	mappedDataPoints["hec"] = hecDataPoints
	mappedDataPoints["thermafuser"] = thermafuserDataPoints
	mappedDataPoints["vav"] = vavDataPoints
	mappedDataPoints["sav"] = savDataPoints

	return mappedDataPoints

def printMappedDataPoints(mappedDataPoints):

	print("AHU datapoints")
	for dataPoint in mappedDataPoints["ahu"]:
		controlProgram = dataPoint[0]
		mappedDataPoint = dataPoint[1]
		print(controlProgram, mappedDataPoint.databaseMapping)

	print("\nVFD datapoints")
	for dataPoint in mappedDataPoints["vfd"]:
		controlProgram = dataPoint[0]
		mappedDataPoint = dataPoint[1]
		print(controlProgram, mappedDataPoint.databaseMapping)

	print("\nFan datapoints")
	for dataPoint in mappedDataPoints["fan"]:
		controlProgram = dataPoint[0]
		mappedDataPoint = dataPoint[1]
		print(controlProgram, mappedDataPoint.databaseMapping)

	print("\nFilter datapoints")
	for dataPoint in mappedDataPoints["filter"]:
		controlProgram = dataPoint[0]
		mappedDataPoint = dataPoint[1]
		print(controlProgram, mappedDataPoint.databaseMapping)

	print("\nDamper datapoints")
	for dataPoint in mappedDataPoints["damper"]:
		controlProgram = dataPoint[0]
		mappedDataPoint = dataPoint[1]
		print(controlProgram, mappedDataPoint.databaseMapping)

	print("\nHEC datapoints")
	for dataPoint in mappedDataPoints["hec"]:
		controlProgram = dataPoint[0]
		mappedDataPoint = dataPoint[1]
		print(controlProgram, mappedDataPoint.databaseMapping)

	print("\nThermafuser datapoints")
	for dataPoint in mappedDataPoints["thermafuser"]:
		controlProgram = dataPoint[0]
		mappedDataPoint = dataPoint[1]
		print(controlProgram, mappedDataPoint.databaseMapping)

	print("\nVAV datapoints")
	for dataPoint in mappedDataPoints["vav"]:
		controlProgram = dataPoint[0]
		mappedDataPoint = dataPoint[1]
		print(controlProgram, mappedDataPoint.databaseMapping)

	print("\nSAV datapoints")
	for dataPoint in mappedDataPoints["sav"]:
		controlProgram = dataPoint[0]
		mappedDataPoint = dataPoint[1]
		print(controlProgram, mappedDataPoint.databaseMapping)


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
		#zonecsvToDb(zone4FilepATH, session, "4")
		print("writting sucessfull")
	except:
		print("Error writting to the database")

	mappedDataPoints = MapDataPoints(session)

	printMappedDataPoints(mappedDataPoints)

	session.close()



#invoke main
main()




