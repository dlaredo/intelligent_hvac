#!/usr/bin/python
import MySQLdb
import csv
import sqlalchemy
import hvacDBMapping
from sqlalchemy.orm import sessionmaker
import traceback

def connect_db():
	"""Function used to connect to the database through MySQLdb"""

	db = None

	try:
		db = MySQLdb.connect(host="localhost", user="dlaredorazo", passwd="@Dexsys13", db="HVAC2")
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
		sqlengine = sqlalchemy.create_engine("mysql+mysqldb://dlaredorazo:@Dexsys13@localhost:3306/HVAC2")
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
	finally:
		session.close()

	#query example
	for instance in session.query(hvacDBMapping.DataPoint).order_by(hvacDBMapping.DataPoint._path):
		print(instance.path, instance.point)

	#inserting with references example
	ahu1 = hvacDBMapping.AHU()


#invoke main
main()