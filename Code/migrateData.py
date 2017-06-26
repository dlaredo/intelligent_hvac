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
				dataPoint = hvacDBMapping.DataPoint(path = row[6], server = row[0], location = row[1], branch = row[2], subBranch = row[3], controlProgram = row[4], point = row[5], zone = zone)
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

	componentNumber = 0
	matchComponentNumber = numberRegex.search(dataString) #Look for the number of the component and create a new component for each new component number found

	if matchComponentNumber:
		componentNumber = int(matchComponentNumber.group())

	return componentNumber


def StoreAHUDataPoints(session):

	#Find AHU-involved data points
	ahu_involved = session.query(DataPoint).filter(DataPoint._path.like('%ahu%')).all()
	ahus = list()
	dampers = list()

	ahu_numbers = set()
	fan_ids = set()

	fanDatapoints = set()
	damperDatapoints = set()
	filterDatapoints = set()
	hecDatapoints = set()
	ahuDataPoints = set()

	damperId = session.query(Damper).count()
	fanId = session.query(Fan).count()

	#Separate AHU, HEC, Fan and Damper information 

	#Regular expressions
	numberRegex = re.compile(r'\d+', flags = re.IGNORECASE)
	damperRegex = re.compile(r'damper', flags = re.IGNORECASE)
	fanRegex = re.compile(r'fan', flags = re.IGNORECASE)

	for dataPoint in ahu_involved:
		
		matchDamper = damperRegex.search(dataPoint.point) #Determine if this point belongs to a damper
		matchFan = fanRegex.search(dataPoint.point) #Determine if this point belongs to a damper

		ahuNumber = determineComponentNumber(numberRegex, dataPoint.path)

		if ahuNumber != 0 and ahuNumber not in ahu_numbers:
			ahu_numbers.add(ahuNumber)
			ahus.append(AHU(ahuNumber))

		#If the point belongs to a damper
		if matchDamper:
			ahu = getAHUByAHUNumber(ahuNumber, ahus)

			splitPath = dataPoint.path.split("/")
			print(splitPath, len(splitPath))
			componentNumber = determineComponentNumber(numberRegex, dataPoint.path.split("/")[1])

			if ahu != None:
				damper = Damper(damperId + 1, ahuNumber, ahu = ahu)
				damperNumber += 1
				print("damper -> ", str(damper.damperId), str(damper.AHUNumber), dataPoint.path)
				damperDatapoints.add(dataPoint)
			else:
				print("AHU not found")

		#If the point belongs to a fan
		if matchFan:
			ahu = getAHUByAHUNumber(ahuNumber, ahus)

			if ahu != None:

				componentNumber = determineComponentNumber(numberRegex, dataPoint.path.split("/")[1])

				if componentNumber not in fan_numbers:
					print(dataPoint.path, "fan Number = ", componentNumber)
					fan_numbers.add()


					fan = Fan(fanNumber + 1, ahuNumber, ahu = ahu)
					fanNumber += 1
					#print("fan -> ", str(fan.fanNumber), str(fan.AHUNumber), dataPoint.path)
					fanDatapoints.add(dataPoint)
			else:
				print("AHU not found")
				
	for ahu in ahus:
		pass
		#print(ahu)

	session.close()


def main():
	"""Main function"""

	zone4FilepATH = "/Users/davidlaredorazo/Desktop/Zone4.csv"
	
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




