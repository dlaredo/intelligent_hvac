import csv
import sqlalchemy
import logging
import traceback
import re
import os
from dateutil.parser import *
from hvacDBMapping import *
from sqlalchemy.orm import sessionmaker
from datetime import datetime

global numberRegex, componentsList, componentsClasses 
componentsList = ["ahu", "vfd", "filter", "damper", "fan", "hec", "sav", "vav", "thermafuser"]
componentsClasses = {"ahu":AHU, "vfd":VFD, "filter":Filter, "damper":Damper, "fan":Fan, "hec":HEC, "sav":SAV, "vav":VAV, "thermafuser":Thermafuser}
numberRegex = re.compile(r'\d+', flags = re.IGNORECASE)


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


def getComponentReadingClassByPathMapping(pathMapping):
	"""Given the path mapping of a point, get the class that it belongs to"""

	componentClass = None

	if pathMapping.componentType == "AHU":
		componentClass = AHUReading
	elif pathMapping.componentType == "VFD":
		componentClass = VFDReading
	elif pathMapping.componentType == "Filter":
		componentClass = FilterReading
	elif pathMapping.componentType == "Damper":
		componentClass = DamperReading
	elif pathMapping.componentType == "Fan":
		componentClass = FanReading
	elif pathMapping.componentType == "HEC":
		componentClass = HECReading
	elif pathMapping.componentType == "SAV":
		componentClass = SAVReading
	elif pathMapping.componentType == "VAV":
		componentClass = VAVReading
	elif pathMapping.componentType == "Thermafuser":
		componentClass = ThermafuserReading
	else:
		componentClass = None

	return componentClass


def fillReadingsInDatabase(dataFolder, mappedDataPoints, session):
	"""Take the mapped datapoints and fill the corresponding readings in the database"""

	header = None
	count = 0

	if os.path.isdir(dataFolder) == False:
		print("Path " + dataFolder + " does not exist")
		logging.error("Path " + dataFolder + " does not exist")
		return

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

					readingClasses = dict()
					rowCount = 0
					readings = list()
					
					reader = csv.reader(csvfile)
					for row in reader:

						columnCount = 0
						
						#get the header and the mapped data points
						if rowCount == 0 and headerMapped == False:
							header = row

							for i in range(1, len(header)):
								header[i] = header[i].replace("[","")
								header[i] = header[i].replace("]","")
								header[i] = header[i].replace("'","")
								header[i] = header[i].replace(" ","")
								mdataPoint = getMappedPoint(header[i], mappedDataPoints)

								if mdataPoint != None:
									fileTypeMappedDataPoints.append(mdataPoint)
								else:
									print("Point not mapped " + header[i])
									logging.warning("Point not mapped " + header[i])

							
							#header is just mapped once per folder, no need to map it more than once per folder
							headerMapped = True
							rowCount += 1
						elif rowCount == 0:
							rowCount += 1
						else:

							time = row[0]
							timestamp = parse(time, None, ignoretz = True)
							#print(len(row), len(fileTypeMappedDataPoints))
							#for j in range(1, len(row) - 1):
							for j in range(1, len(fileTypeMappedDataPoints)+1):

								i = j-1

								componentFound = False

								if fileTypeMappedDataPoints[i].pathMapping != None and fileTypeMappedDataPoints[i].componentId != None:

									componentClass = getComponentReadingClassByPathMapping(fileTypeMappedDataPoints[i].pathMapping)

									#Create new component if necessary or retrieve an existing one to store the reading
									if fileTypeMappedDataPoints[i].pathMapping.componentType in readingClasses:
										if fileTypeMappedDataPoints[i].componentId in readingClasses[fileTypeMappedDataPoints[i].pathMapping.componentType]:
											reading = readingClasses[fileTypeMappedDataPoints[i].pathMapping.componentType][fileTypeMappedDataPoints[i].componentId]
										else:
											reading = componentClass(None, fileTypeMappedDataPoints[i].componentId)
											readingClasses[fileTypeMappedDataPoints[i].pathMapping.componentType][fileTypeMappedDataPoints[i].componentId] = reading
									else:
										readingClasses[fileTypeMappedDataPoints[i].pathMapping.componentType] = dict()
										reading = componentClass(None, fileTypeMappedDataPoints[i].componentId)
										readingClasses[fileTypeMappedDataPoints[i].pathMapping.componentType][fileTypeMappedDataPoints[i].componentId] = reading

									#Set the current column value in its corresponding attribute in the components
									attribute = fileTypeMappedDataPoints[i].pathMapping.databaseMapping
									setattr(reading, attribute, row[j])

								else:
									if fileTypeMappedDataPoints[i].pathMapping == None:
										print(header[i], "Point not mapped")
										logging.warning(header[i], "Point not mapped")
									else:
										print(header[i], "Component not found")
										logging.warning(header[i], "Component not found")

							for key1 in readingClasses:
								for key2 in readingClasses[key1]:

									readingClasses[key1][key2].timestamp = timestamp
									new_object = copy_sqla_object(readingClasses[key1][key2], omit_fk = False)
									readings.append(new_object)
									session.add(new_object)  #Add the readings to the database


					session.commit()

	print("Finished migration " + dataFolder)
	logging.info("Finished migration " + dataFolder)


def main():
	"""Main function"""

	#Order of the function calls matters in this function, do not change it.

	dataFolder = "/Users/davidlaredorazo/Desktop/Zone12"
	database = "mysql+mysqldb://dlaredorazo:@Dexsys13@localhost:3306/HVAC2"
	
	#set the logger config
	logging.basicConfig(filename='migrateData.log', level=logging.INFO,\
	format='%(levelname)s:%(threadName)s:%(asctime)s:%(filename)s:%(funcName)s:%(message)s', datefmt='%m/%d/%Y %H:%M:%S')

	logging.info("Started migrating from csv files")

	#Attempt connection to the database
	try:
		sqlengine = sqlalchemy.create_engine(database)
		Session = sessionmaker(bind=sqlengine)
		session = Session()

		print("Connection to " + database + " successfull")
		logging.info("Connection to " + database + " successfull")
	except Exception as e:
		logging.error("Error in connection to the database")
		logging.error(traceback.format_exc())
		print("Error in connection to the database")
		return False

	#get the datapoints
	mappedDataPoints = {key:session.query(DataPoint).join(PathMapping).filter(PathMapping._componentType == key).all() for key in componentsList}

	print("Migrating from csv files")
	logging.info("Migrating from csv files")
	fillReadingsInDatabase(dataFolder, mappedDataPoints, session)

	session.close()

	logging.info("Finished migrating from csv files")


#invoke main
main()




