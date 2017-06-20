#!/usr/bin/python
import MySQLdb

def connect_db():

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

#Main
db = connect_db()

