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
	matchComponentNumber = numberRegex.findall(pathString)

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

	for key in mappedDataPoints:

		componentDataPoints = len(mappedDataPoints[key])
		totalDataPoints += componentDataPoints

		print("\n" + key + " datapoints = ", componentDataPoints)

		for mappedDataPoint in mappedDataPoints[key]:
			print(mappedDataPoint.path, mappedDataPoint.controlProgram, mappedDataPoint.pathMapping.databaseMapping)

	print("\nTotal data points = ", totalDataPoints)

def printComponents(components):

	for ahu in components["ahu"]:
		print("AHU Number: " + str(ahu.AHUNumber) + ", AHU Name: " + str(ahu.AHUName))
	for vfd in components["vfd"]:
		print("VFD Number: " + str(vfd.vfdId) + ", VFD Name: " + str(vfd.vfdName) + ", Parent AHU: " + str(vfd.AHUNumber))
	for filt in components["filter"]:
		print("Filter Number: " + str(filt.filterId) + ", Filter Name: " + str(filt.filterName) + ", Parent AHU: " + str(filt.AHUNumber))
	for damper in components["damper"]:
		print("Damper Number: " + str(damper.damperId) + ", Damper Name: " + str(damper.damperName) + ", Parent AHU: " + str(damper.AHUNumber))
	for fan in components["fan"]:
		print("Fan Number: " + str(fan.fanId) + ", Fan Name: " + str(fan.fanName) + ", Parent AHU: " + str(fan.AHUNumber))
	for vav in components["vav"]:
		print("VAV Number: " + str(vav.VAVId) + ", VAV Name: " + str(vav.VAVName) + ", Parent AHU: " + str(vav.AHUNumber))


def determineAhu(components, componentNames, relationships, ComponentClass, mappedDataPoint):
	"""Determine the ahu that supplies certain component based on its datapoint"""

	determinedAhu = None

	if ComponentClass == VFD:
		for ahu in components["ahu"]:
			if ahu.AHUName.lower() in mappedDataPoint.controlProgram.lower():
				determinedAhu = ahu

	if ComponentClass == Filter or ComponentClass == Damper or ComponentClass == Fan:
		for ahu in components["ahu"]:
			if ahu.AHUName.lower() in mappedDataPoint.path.lower():
				determinedAhu = ahu


	#Determination of AHU for VAV and SAV needs to be improved for performance since a search in a list is performed everytime
	if ComponentClass == VAV:
		for relationship in relationships["vav"]:
			if relationship.componentName.lower() == mappedDataPoint.controlProgram.lower():
				ahuName = relationship.parentComponent
				for ahu in components["ahu"]:
					if ahu.AHUName.lower() in ahuName.lower():
						determinedAhu = ahu

	if ComponentClass == SAV:
		for relationship in relationships["sav"]:
			if relationship.componentName.lower() == mappedDataPoint.controlProgram.lower():
				ahuName = relationship.parentComponent
				for ahu in components["ahu"]:
					if ahu.AHUName.lower() in ahuName.lower():
						determinedAhu = ahu
				
	return determinedAhu


def determineComponentType(componentClass, dataPoint):
	"""Determine component type based on its dataPoint"""

	componentType = ""

	if componentClass == VFD:
		if "supply" in dataPoint.controlProgram.lower() or "supply" in dataPoint.path.lower():
			componentType = "Supply"
		elif "return" in dataPoint.controlProgram.lower() or "return" in dataPoint.path.lower():
			componentType = "Return"
		else:
			componentType = ""
	elif componentClass == Filter:
		if "final" in dataPoint.point.lower() or "ffilter" in dataPoint.path.lower():
			componentType = "Final"
		elif "pre" in dataPoint.point.lower() or "pfilter" in dataPoint.path.lower():
			componentType = "Pre"
		else:
			componentType = ""
	elif componentClass == Damper:
		if "ra" in dataPoint.point.lower() or "ra" in dataPoint.path.lower():
			componentType = "Return Air"
		elif "oa" in dataPoint.point.lower() or "oa" in dataPoint.path.lower():
			componentType = "Outside Air"
		elif "ea" in dataPoint.point.lower() or "ea" in dataPoint.path.lower():
			componentType = "Exhaust Air"
		elif "sa" in dataPoint.point.lower() or "sa" in dataPoint.path.lower():
			componentType = "Supply Air"
		else:
			componentType = ""
	elif componentClass == Fan:
		if "supply" in dataPoint.point.lower() or "sf" in dataPoint.path.lower():
			componentType = "Supply Air"
		elif "return" in dataPoint.point.lower() or "rf" in dataPoint.path.lower():
			componentType = "Return Air"
		elif "exhaust" in dataPoint.point.lower() or "ef" in dataPoint.path.lower():
			componentType = "Exhaust Air"
		elif "outside" in dataPoint.point.lower() or "of" in dataPoint.path.lower():
			componentType = "Exhaust Air"
		else:
			componentType = ""

	return componentType


def appendNewComponents(components, componentNames, relationships, ComponentClass, mappedDataPoints, componentKey, totalNumberOfComponents):
	"""Fill components in a list to be inserted to the database"""

	new_components = list()

	for mdataPoint in mappedDataPoints[componentKey]:

		#componentNumber = determineComponentNumber(mdataPoint.path)
		#print(componentNumber)

		#fill AHUs
		if ComponentClass == AHU:
			
			if mdataPoint.controlProgram not in componentNames[componentKey]:
				components["ahu"].append(ComponentClass(AHUNumber = totalNumberOfComponents + 1, AHUName = mdataPoint.controlProgram))
				componentNames["ahu"].add(mdataPoint.controlProgram)
				totalNumberOfComponents += 1
		#Fill VFDs, Filters, Dampers, Fans
		elif ComponentClass == VFD or ComponentClass == Fan or ComponentClass == Filter or ComponentClass == Damper:

			componentType = determineComponentType(ComponentClass, mdataPoint)

			if ComponentClass == VFD:
				componentName = mdataPoint.controlProgram
			else:
				splittedPath = mdataPoint.path.split("/")
				componentPath = splittedPath[len(splittedPath) - 1]
				componentNumber = determineComponentNumber(componentPath)
				componentName = componentType + " "  + componentKey.title() + " " + str(componentNumber)

			#print(componentName)

			if componentName not in componentNames[componentKey]:
				ahu = determineAhu(components, componentNames, relationships, ComponentClass, mdataPoint)

				if ahu != None and componentType != "":
					component = ComponentClass(totalNumberOfComponents + 1, ahu.AHUNumber, componentName, componentType, ahu)
					#ahu.filters.append(filt)
					components[componentKey].append(component)
					componentNames[componentKey].add(componentName)
					totalNumberOfComponents += 1

					#print(mdataPoint.path, ahu.AHUName)
				else:
					print(mdataPoint.controlProgram, mdataPoint.point, mdataPoint.path)
					if ahu == None:
						print("Could not determine ahu")
					elif componentType == "":
						print("Could not determine componentType")
		#Fill VAVs and SAVs
		elif ComponentClass == VAV or ComponentClass == SAV:
			componentName = mdataPoint.controlProgram

			if componentName not in componentNames[componentKey]:
				ahu = determineAhu(components, componentNames, relationships, ComponentClass, mdataPoint)

				if ahu != None:
					component = ComponentClass(totalNumberOfComponents + 1, ahu.AHUNumber, componentName, ahu)
					#ahu.filters.append(filt)
					components[componentKey].append(component)
					componentNames[componentKey].add(componentName)
					totalNumberOfComponents += 1

					#print(mdataPoint.path, ahu.AHUName)
				else:
					print(mdataPoint.controlProgram, mdataPoint.point, mdataPoint.path)
					print("Could not determine ahu")

	return new_components


def fillComponentsInDatabase(mappedDataPoints, session):
	"""Take the mapped datapoints and fill the corresponding components in the database"""

	#data structures
	componentNames = dict()
	componentNames["ahu"] = set()
	componentNames["vfd"] = set()
	componentNames["filter"] = set()
	componentNames["damper"] = set()
	componentNames["fan"] = set()
	componentNames["hec"] = set()
	componentNames["sav"] = set()
	componentNames["vav"] = set()
	componentNames["thermafuser"] = set()

	components = dict()
	components["ahu"] = session.query(AHU).all()
	components["vfd"] = session.query(VFD).all()
	components["filter"] = session.query(Filter).all()
	components["damper"] = session.query(Damper).all()
	components["fan"] = session.query(Fan).all()
	components["hec"] = session.query(HEC).all()
	components["sav"] = session.query(SAV).all()
	components["vav"] = session.query(VAV).all()
	components["thermafuser"] = session.query(Thermafuser).all()

	relationships = dict()
	relationships["vav"] = session.query(ComponentRelationship).filter(ComponentRelationship._componentType == "VAV").all()
	relationships["sav"] = session.query(ComponentRelationship).filter(ComponentRelationship._componentType == "SAV").all()
	relationships["themafuser"] = session.query(ComponentRelationship).filter(ComponentRelationship._componentType == "Thermafuser").all()

	for ahu in components["ahu"]:
		componentNames["ahu"].add(ahu.AHUName)
	for vfd in components["vfd"]:
		componentNames["vfd"].add(vfd.vfdName)
	for filt in components["filter"]:
		componentNames["filter"].add(filt.filterName)
	for damper in components["damper"]:
		componentNames["damper"].add(damper.damperName)
	for fan in components["fan"]:
		componentNames["fan"].add(fan.fanName)
	for hec in components["hec"]:
		componentNames["hec"].add(hec.HECName)
	for sav in components["sav"]:
		componentNames["sav"].add(sav.SAVName)
	for vav in components["vav"]:
		componentNames["vav"].add(vav.VAVName)
	for thermafuser in components["thermafuser"]:
		componentNames["thermafuser"].add(thermafuser.thermafuserName)

	#Order in which new elements are appended is important, dont change this order
	appendNewComponents(components, componentNames, relationships, AHU, mappedDataPoints, "ahu", len(components["ahu"]))
	appendNewComponents(components, componentNames, relationships, VFD, mappedDataPoints, "vfd", len(components["vfd"]))
	appendNewComponents(components, componentNames, relationships, Filter, mappedDataPoints, "filter", len(components["filter"]))
	appendNewComponents(components, componentNames, relationships, Damper, mappedDataPoints, "damper", len(components["damper"]))
	appendNewComponents(components, componentNames, relationships, Fan, mappedDataPoints, "fan", len(components["fan"]))
	appendNewComponents(components, componentNames, relationships, VAV, mappedDataPoints, "vav", len(components["vav"]))

	printComponents(components)

	#Commit changes to the database
	for key in components:
		session.add_all(components[key])
	
	session.commit()


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

	#printMappedDataPoints(mappedDataPoints)

	print("Filling components in Database")
	fillComponentsInDatabase(mappedDataPoints, session)

	session.close()



#invoke main
main()




