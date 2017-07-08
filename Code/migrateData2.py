import csv
import sqlalchemy
from hvacDBMapping import *
from sqlalchemy.orm import sessionmaker
import traceback
import datetime
import re
import os


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
			if count == 0:
				count += 1
			else:

				path = row[6]
				if path not in dataPointInserted:
					#add the datapoints to the DB session
					dataPoint = DataPoint(path = path, server = row[0], location = row[1], branch = row[2], subBranch = row[3], controlProgram = row[4], point = row[5], zone = zone)
					dbsession.add(dataPoint)

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
	for sav in components["sav"]:
		print("SAV Number: " + str(sav.VAVId) + ", SAV Name: " + str(sav.VAVName) + ", Parent AHU: " + str(sav.AHUNumber))
	for hec in components["hec"]:
		print("HEC Number: " + str(hec.HECId) + ", HEC Name: " + str(hec.HECName) + ", Parent AHU: " + str(hec.AHUNumber) +
		", Parent VAV: " + str(hec.VAVId)  + ", Parent SAV: " + str(hec.SAVId))
	for thermafuser in components["thermafuser"]:
		print("THR Number: " + str(thermafuser.thermafuserId) + ", THR Name: " + str(thermafuser.thermafuserName) + ", Parent AHU: " + str(thermafuser.AHUNumber) + 
		", Parent VAV: " + str(thermafuser.VAVId) + ", Parent SAV: " + str(thermafuser.SAVId))


def getParentComponent(components, componentNames, relationships, ComponentClass, parentComponentType, mappedDataPoint):
	"""Determine the ahu that supplies certain component based on its datapoint"""

	determinedParent = None

	if ComponentClass == VFD:
		for ahu in components["ahu"]:
			if ahu.AHUName.lower() in mappedDataPoint.controlProgram.lower():
				determinedParent = ahu

	if ComponentClass == Filter or ComponentClass == Damper or ComponentClass == Fan:
		for ahu in components["ahu"]:
			if ahu.AHUName.lower() in mappedDataPoint.path.lower():
				determinedParent = ahu


	#Determination of AHU for VAV and SAV needs to be improved for performance since a search in a list is performed everytime
	if ComponentClass == VAV:
		for relationship in relationships["vav"]:
			if relationship.componentName.lower() == mappedDataPoint.controlProgram.lower():
				ahuName = relationship.parentComponent
				for ahu in components["ahu"]:
					if ahu.AHUName.lower() == ahuName.lower():
						determinedParent = ahu

	if ComponentClass == SAV:
		for relationship in relationships["sav"]:
			if relationship.componentName.lower() == mappedDataPoint.controlProgram.lower():
				ahuName = relationship.parentComponent
				for ahu in components["ahu"]:
					if ahu.AHUName.lower() == ahuName.lower():
						determinedParent = ahu

	if ComponentClass == Thermafuser:
		for relationship in relationships["thermafuser"]:
			if relationship.componentName.lower() == mappedDataPoint.controlProgram.lower():
				parentName = relationship.parentComponent

				#Look for the parent component in either ahus, savs or vavs.
				#Determination of parent for Thermafuser needs to be improved for performance since a search in 3 lists is performed everytime
				for ahu in components["ahu"]:
					if ahu.AHUName.lower() == parentName.lower():
						determinedParent = ahu
				for vav in components["vav"]:
					if vav.VAVName.lower() == parentName.lower():
						determinedParent = vav
				for sav in components["sav"]:
					if sav.SAVName.lower() == parentName.lower():
						determinedParent = sav

	if ComponentClass == HEC:
		if parentComponentType == "AHU":
			for parent in components["ahu"]:
				if parent.AHUName.lower() in mappedDataPoint.controlProgram.lower():
					determinedParent = parent
		if parentComponentType == "VAV":
			for parent in components["vav"]:
				if parent.VAVName.lower() in mappedDataPoint.controlProgram.lower():
					determinedParent = parent
		if parentComponentType == "SAV":
			for parent in components["sav"]:
				if parent.SAVName.lower() in mappedDataPoint.controlProgram.lower():
					determinedParent = parent
				
	return determinedParent


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
	elif componentClass == HEC:
		if "cw" in dataPoint.point.lower() or "chw" in dataPoint.path.lower():
			componentType = "Cold Water"
		elif "hw" in dataPoint.point.lower() or "hw" in dataPoint.path.lower():
			componentType = "Hot Water"
		else:
			componentType = ""
	elif componentClass == Thermafuser:
		componentType = "Thermafuser"

	return componentType


def appendNewComponents(components, componentNames, relationships, ComponentClass, mappedDataPoints, componentKey, totalNumberOfComponents):
	"""Fill components in a list to be inserted to the database"""

	new_components = list()

	for mdataPoint in mappedDataPoints[componentKey]:

		#fill AHUs
		if ComponentClass == AHU:
			
			componentName = mdataPoint.controlProgram
			if mdataPoint.controlProgram not in componentNames[componentKey]:
				components[componentKey].append(ComponentClass(AHUNumber = totalNumberOfComponents + 1, AHUName = mdataPoint.controlProgram))
				#componentNames[componentKey].add(mdataPoint.controlProgram)
				totalNumberOfComponents += 1
				mdataPoint.componentId = totalNumberOfComponents
				componentNames[componentKey][componentName] = mdataPoint.componentId
			else:
				mdataPoint.componentId = componentNames[componentKey][componentName]

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
				ahu = getParentComponent(components, componentNames, relationships, ComponentClass, "AHU", mdataPoint)

				if ahu != None and componentType != "":
					component = ComponentClass(totalNumberOfComponents + 1, ahu.AHUNumber, componentName, componentType, ahu)
					#ahu.filters.append(filt)
					components[componentKey].append(component)
					#componentNames[componentKey].add(componentName)
					totalNumberOfComponents += 1
					mdataPoint.componentId = totalNumberOfComponents
					componentNames[componentKey][componentName] = mdataPoint.componentId

					#print(mdataPoint.path, ahu.AHUName)
				else:
					print(mdataPoint.controlProgram, mdataPoint.point, mdataPoint.path)
					if ahu == None:
						print("Could not determine ahu")
					elif componentType == "":
						print("Could not determine componentType")
			else:
				mdataPoint.componentId = componentNames[componentKey][componentName]

		#Fill VAVs and SAVs
		elif ComponentClass == VAV or ComponentClass == SAV:
			componentName = mdataPoint.controlProgram

			if componentName not in componentNames[componentKey]:
				ahu = getParentComponent(components, componentNames, relationships, ComponentClass, "AHU", mdataPoint)

				if ahu != None:
					component = ComponentClass(totalNumberOfComponents + 1, ahu.AHUNumber, componentName, ahu)
					#ahu.filters.append(filt)
					components[componentKey].append(component)
					#componentNames[componentKey].add(componentName)
					totalNumberOfComponents += 1
					mdataPoint.componentId = totalNumberOfComponents
					componentNames[componentKey][componentName] = mdataPoint.componentId

					#print(mdataPoint.path, ahu.AHUName)
				else:
					print(mdataPoint.controlProgram, mdataPoint.point, mdataPoint.path)
					print("Could not determine ahu")
			else:
				mdataPoint.componentId = componentNames[componentKey][componentName]

		#Fill HECs and thermafusers
		elif ComponentClass == HEC or Thermafuser:
			componentType = determineComponentType(ComponentClass, mdataPoint)

			#Determine parent component
			if "AHU" in mdataPoint.controlProgram:
				parentComponentType = "AHU"
			elif "VAV" in mdataPoint.controlProgram:
				parentComponentType = "VAV"
			elif "SAV" in mdataPoint.controlProgram:
				parentComponentType = "SAV"
			else:  #Thermafuser case, we dont know what its parent component type is a priory
				parentComponentType = ""
			
			#Try to determine its parent component
			parentComponent = getParentComponent(components, componentNames, relationships, ComponentClass, parentComponentType, mdataPoint)

			if parentComponent != None:
				parentComponentName = parentComponent.getComponentName()

				#Form componentName
				if ComponentClass == HEC:
					splittedPath = mdataPoint.path.split("/")
					componentPath = splittedPath[len(splittedPath) - 1]
					componentNumber = determineComponentNumber(componentPath)
					componentName = parentComponentName + "/" + componentType + " "  + componentKey.title() + " " + str(componentNumber)
				else:
					componentName = parentComponentName + "/" + mdataPoint.controlProgram
			
				#print(componentName, mdataPoint.path)

				if componentName not in componentNames[componentKey]:
			
					#Create the new component
					if parentComponent.getComponentType() == "AHU":
						if ComponentClass == HEC:
							component = ComponentClass(totalNumberOfComponents + 1, componentName, componentType, AHUNumber = parentComponent.AHUNumber, ahu = parentComponent)
							#ahu.hecs.append(component)
						else:
							component = ComponentClass(totalNumberOfComponents + 1, componentName, AHUNumber = parentComponent.AHUNumber, ahu = parentComponent)
							#ahu.thermafusers.append(component)
					elif parentComponent.getComponentType() == "VAV":
						if ComponentClass == HEC:
							component = ComponentClass(totalNumberOfComponents + 1, componentName, componentType, VAVId = parentComponent.VAVId, vav = parentComponent)
							#vav.hecs.append(component)
						else:
							component = ComponentClass(totalNumberOfComponents + 1, componentName, VAVId = parentComponent.VAVId, vav = parentComponent)
							#vav.thermafusers.append(component)
					elif parentComponent.getComponentType() == "SAV":
						if ComponentClass == HEC:
							component = ComponentClass(totalNumberOfComponents + 1, componentName, componentType, SAVId = parentComponent.SAVId, sav = parentComponent)
							#sav.hecs.append(component)
						else:
							component = ComponentClass(totalNumberOfComponents + 1, componentName, SAVId = parentComponent.SAVId, sav = parentComponent)
							#sav.thermafusers.append(component)
					else:
						print("Undetermined parent component " + parentComponent.getComponentType())
						continue

					components[componentKey].append(component)
					#componentNames[componentKey].add(componentName)
					totalNumberOfComponents += 1
					mdataPoint.componentId = totalNumberOfComponents
					componentNames[componentKey][componentName] = mdataPoint.componentId
				else:
					mdataPoint.componentId = componentNames[componentKey][componentName]

			else:
				print(mdataPoint.controlProgram, mdataPoint.point, mdataPoint.path)
				print("Could not determine parent " + parentComponentType)


	return new_components


def fillComponentsInDatabase(mappedDataPoints, session):
	"""Take the mapped datapoints and fill the corresponding components in the database"""

	#data structures
	componentNames = dict()
	componentNames["ahu"] = dict()
	componentNames["vfd"] = dict()
	componentNames["filter"] = dict()
	componentNames["damper"] = dict()
	componentNames["fan"] = dict()
	componentNames["hec"] = dict()
	componentNames["sav"] = dict()
	componentNames["vav"] = dict()
	componentNames["thermafuser"] = dict()

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
	relationships["thermafuser"] = session.query(ComponentRelationship).filter(ComponentRelationship._componentType == "Thermafuser").all()

	for ahu in components["ahu"]:
		componentNames["ahu"][ahu.AHUName] = ahu.AHUNumber
	for vfd in components["vfd"]:
		componentNames["vfd"][vfd.vfdName] = vfd.vfdId
	for filt in components["filter"]:
		componentNames["filter"][filt.filterName] = filt.filterId
	for damper in components["damper"]:
		componentNames["damper"][damper.damperName] = damper.damperId
	for fan in components["fan"]:
		componentNames["fan"][fan.fanName] = fan.fanId
	for hec in components["hec"]:
		componentNames["hec"][hec.HECName] = hec.HECId
	for sav in components["sav"]:
		componentNames["sav"][sav.SAVName] = sav.SAVId
	for vav in components["vav"]:
		componentNames["vav"][vav.VAVName] = vav.VAVId
	for thermafuser in components["thermafuser"]:
		componentNames["thermafuser"][thermafuser.thermafuserName] = thermafuser.thermafuserId

	#Order in which new elements are appended is important, dont change this order
	appendNewComponents(components, componentNames, relationships, AHU, mappedDataPoints, "ahu", len(components["ahu"]))
	appendNewComponents(components, componentNames, relationships, VFD, mappedDataPoints, "vfd", len(components["vfd"]))
	appendNewComponents(components, componentNames, relationships, Filter, mappedDataPoints, "filter", len(components["filter"]))
	appendNewComponents(components, componentNames, relationships, Damper, mappedDataPoints, "damper", len(components["damper"]))
	appendNewComponents(components, componentNames, relationships, Fan, mappedDataPoints, "fan", len(components["fan"]))
	appendNewComponents(components, componentNames, relationships, VAV, mappedDataPoints, "vav", len(components["vav"]))
	appendNewComponents(components, componentNames, relationships, SAV, mappedDataPoints, "sav", len(components["sav"]))
	appendNewComponents(components, componentNames, relationships, HEC, mappedDataPoints, "hec", len(components["hec"]))
	appendNewComponents(components, componentNames, relationships, Thermafuser, mappedDataPoints, "thermafuser", len(components["thermafuser"]))

	#printComponents(components)

	#Commit changes to the database
	for key in components:
		session.add_all(components[key])

	#session.add_all(mappedDataPoints)
	
	session.commit()

def getMappedPoint(dataPointPath, mappedDataPoints):
	"""For each data point in the database, get its mapped datapoint that contains all the information regarding how such data point maps to the database"""

	#This can be improved for better performance, since for each data point it has to look through all the datapoints which is of quadratic complexity

	mdataPoint = None

	for key in mappedDataPoints:
		for mappedDataPoint in mappedDataPoints[key]:
			#print(dataPointPath, mappedDataPoint.path)
			if mappedDataPoint.path == dataPointPath:

				mdataPoint = mappedDataPoint
				break

	return mdataPoint



def fillReadingsInDatabase(dataFolder, mappedDataPoints, session):
	"""Take the mapped datapoints and fill the corresponding readings in the database"""

	header = None
	count = 0

	for root, dirs, files in os.walk(dataFolder):
		
		print(root)

		headerMapped = False
		fileTypeMappedDataPoints = list()

		for csvFile in files:

			splittedPath = os.path.splitext(csvFile)
			extension = splittedPath[len(splittedPath) - 1]
			
			#Verify if the file is a csv file
			if extension == ".csv":
				fullpath = os.path.join(root,csvFile)

				#Open the csv file
				with open(os.path.join(root,csvFile), 'r') as csvfile:

					columnCount = 0
					rowCount = 0
					
					reader = csv.reader(csvfile)
					for row in reader:
						
						#get the header and the mapped data points
						if rowCount == 0 and headerMapped == False:
							header = row

							for i in range(1, len(header)):
								header[i] = header[i].replace("[","")
								header[i] = header[i].replace("]","")
								header[i] = header[i].replace("'","")
								header[i] = header[i].replace(" ","")
								mdataPoint = getMappedPoint(header[i], mappedDataPoints)

								if mdataPoint.pathMapping != None:
									fileTypeMappedDataPoints.append(mdataPoint)
								else:
									print(header[i], "Point not mapped")

								columnCount += 1
							
							print(header)
							headerMapped = True
							rowCount += 1
						elif rowCount == 0:
							rowCount += 1
						else:
							print(row)


def main():
	"""Main function"""

	#Order of the function calls matters in this function, do not change it.

	zone4FilepATH = "../csv_files/Zone4.csv"
	dataFolder = "/Users/davidlaredorazo/Box Sync/Data/Zone4"
	
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

	print("Migrating from csv files")
	fillReadingsInDatabase(dataFolder, mappedDataPoints, session)

	session.close()


#invoke main
main()




