#!/usr/bin/python
import MySQLdb
import csv
import sqlalchemy
import hvacDBMapping
from sqlalchemy.orm import sessionmaker
import traceback
import datetime

def connect_db():
	"""Function used to connect to the database through MySQLdb"""

	db = None

	try:
		db = MySQLdb.connect(host="localhost", user="dlaredorazo", passwd="@Dexsys13", db="HVAC")
		cursor = db.cursor()
		cursor.execute("SELECT VERSION()")
		results = cursor.fetchone()
		ver = results[0]

		if (ver is None):
			print("Error in connection")
			#return False
		else:
			print("Connection successfull")
			#return True
	except:
		print("Error in connection")
		#return False

	return db

def csvToDb(filepath, dbsession, zone):
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


def main():
	"""Main function"""

	#db = connect_db()
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
	try:
		#csvToDb(zone4FilepATH, session, "4")
		print("writting sucessfull")
	except Exception as e:
		print(traceback.format.exc())
		print("writing error")
		return False

	#query example
	for instance in session.query(hvacDBMapping.DataPoint).order_by(hvacDBMapping.DataPoint._path):
		print(instance.path, instance.point)

	now = datetime.datetime.now()
	filterReading11 = hvacDBMapping.FilterReading(now, 1, "Type 1", 0.85, None)
	filterReading21 = hvacDBMapping.FilterReading(now, 2, "Type 1", 0.85, None)
	filterReading31 = hvacDBMapping.FilterReading(now, 3, "Type 1", 0.85, None)
	filterReading41 = hvacDBMapping.FilterReading(now, 4, "Type 1", 0.85, None)

	now = datetime.datetime.now() + datetime.timedelta(minutes = 1)
	filterReading12 = hvacDBMapping.FilterReading(now, 1, "Type 2", 0.95, None)
	filterReading22 = hvacDBMapping.FilterReading(now, 2, "Type 2", 0.95, None)
	filterReading32 = hvacDBMapping.FilterReading(now, 3, "Type 2", 0.95, None)
	filterReading42 = hvacDBMapping.FilterReading(now, 4, "Type 2", 0.95, None)


	filter1 = hvacDBMapping.Filter(1, 1, None, [])
	filter2 = hvacDBMapping.Filter(2, 1, None, [])
	filter3 = hvacDBMapping.Filter(3, 1, None, [])
	filter4 = hvacDBMapping.Filter(4, 1, None, [])

	#inserting with references example
	ahu1 = hvacDBMapping.AHU(1, filters = [])

	#configure relationships
	filterReading11.filter = filter1
	filterReading21.filter = filter2
	filterReading31.filter = filter3
	filterReading41.filter = filter4
	filterReading12.filter = filter1
	filterReading22.filter = filter2
	filterReading32.filter = filter3
	filterReading42.filter = filter4

	#print(filterReading41)
	#print(filterReading42)

	filter1.filterReadings = [filterReading11, filterReading12]
	filter2.filterReadings = [filterReading21, filterReading22]
	filter3.filterReadings = [filterReading31, filterReading32]
	filter4.filterReadings = [filterReading41, filterReading42]


	filter1.ahu = ahu1
	filter2.ahu = ahu1
	filter3.ahu = ahu1
	filter4.ahu = ahu1

	#print(filter1)
	#print(filter2)
	#print(filter3)
	#print(filter4)

	ahu1.filters = [filter1, filter2, filter3, filter4]

	print(ahu1)

	try:
		session.add(ahu1)
		session.commit()
		print("writing of object: success")
	except Exception as e:
		print(traceback.format.exc())
		print("writing of object: error")
		return False
	finally:
		session.close()


#invoke main
main()