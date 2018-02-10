import web
import sqlalchemy
from damadicsDBMapping import ValveReading
from datetime import datetime
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker

urls = (
    '/getSimulatedData', 'SimulatedData'
)

globalSession = None

class SimulatedData:

	def __init__(self):
		self.session = getDBSession()

	def POST(self):

		web.header('Access-Control-Allow-Origin',      '*')
		web.header('Access-Control-Allow-Credentials', 'true')

		if self.session == None:
			return "Nonexistent session"

		#Input parameters, dateTime to retrieve data, number of values to retrieve, name of the measurement to display
		data = web.input()
		dateTime = datetime.strptime(data.dateTime, '%m/%d/%Y %H:%M:%S')
		nValues = int(data.nValues)
		measurementName = data.mName



		print(dateTime)
		print(nValues)
		dataValues = self.session.query(ValveReading).filter(ValveReading._timestamp >= dateTime).limit(nValues).all()

		results = [getattr(dataValue, measurementName) for dataValue in dataValues]

		return results

def getDBSession():
	"""Attempt to connect to the database an get a session to it"""

	engineType = "mysql+mysqldb://"
	db = "damadics2"
	host = "localhost"
	port = "3306"
	user = "readOnly"
	password = "readOnly"
	databaseString = engineType + user + ":" + password + "@" + host + ":" + port + "/" + db
	session = None

	#Attempt connection to the database
	try:
		sqlengine = sqlalchemy.create_engine(databaseString)
		Session = sessionmaker(bind=sqlengine)
		session = Session()

		print("Connection to " + engineType + host + ":" + port + "/" + db + " successfull")
	except Exception as e:
		print(traceback.format.exc())
		print("Error in connection to " + engineType + host + ":" + port + "/" + db)
		return False

	return session


if __name__ == "__main__":

	#global globalSession
	#dbsession = getDBSession()

	#if dbsession == None:
	#	exit()

	#globalSession = dbsession
	#print(globalSession)
	app = web.application(urls, globals())
	app.run()