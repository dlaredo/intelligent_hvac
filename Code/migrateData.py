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

def StoreAHUDataPoints(session):
	"""Store all the data points corresponding to AHUs"""

	#Find AHU-involved data points
	ahu_involved = session.query(DataPoint).filter(DataPoint._path.like('%ahu%')).all()

	#Find the already stored AHUs
	ahus = session.query(AHU).all()

	new_ahus = list()
	dampers = list()

	ahu_numbers, ahu_fan_numbers, ahu_damper_numbers, ahu_hec_numbers, ahu_filter_numbers = getStoredAHUComponentsId(ahus)

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
		matchFan = fanRegex.search(dataPoint.point) #Determine if this point belongs to a fan

		ahuNumber = determineComponentNumber(numberRegex, dataPoint.path)

		if ahuNumber != 0 and ahuNumber not in ahu_numbers:
			ahu_numbers.add(ahuNumber)
			ahus.append(AHU(ahuNumber))

			ahu_fan_numbers[ahuNumber] = set()
			ahu_damper_numbers[ahuNumber] = set()
			ahu_hec_numbers[ahuNumber] = set()
			ahu_filter_numbers[ahuNumber] = set()

		ahu = getAHUByAHUNumber(ahuNumber, ahus)

		if ahu != None:

			splittedPath = dataPoint.path.split("/")
			componentNumber = determineComponentNumber(numberRegex, splittedPath[len(splittedPath) - 1])

			#If the point belongs to a damper
			if matchDamper:
				if componentNumber not in ahu_damper_numbers[ahu.AHUNumber]:

					damper = Damper(damperId + 1, ahuNumber, componentNumber, ahu = ahu)
					damperId += 1
					print("damper -> ", str(damper.damperId), str(damper.AHUNumber), str(damper.damperNumber), dataPoint.path)
					ahu_damper_numbers[ahu.AHUNumber].add(componentNumber)
					damperDatapoints.add(dataPoint)

			#If the point belongs to a fan
			if matchFan:
				if componentNumber not in ahu_fan_numbers[ahu.AHUNumber]:
					
					fan = Fan(fanId + 1, ahuNumber, componentNumber, ahu = ahu)
					fanId += 1
					print("fan -> ", str(fan.fanId), str(fan.AHUNumber), str(fan.fanNumber), dataPoint.path)
					ahu_fan_numbers[ahu.AHUNumber].add(componentNumber)
					fanDatapoints.add(dataPoint)
		
		else:
			print("AHU not found")
				
	for ahu in ahus:
		pass
		#print(ahu)

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

	#StoreAHUDataPoints(session)



#invoke main
main()




