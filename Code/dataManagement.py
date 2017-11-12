import numpy as np
import pandas as pd
import sqlalchemy
from hvacDBMapping import *
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy import and_
from copy import copy

def getDBSession():
	"""Attempt to connect to the database an get a session to it"""

	engineType = "mysql+mysqldb://"
	db = "HVAC2"
	host = "localhost"
	port = "3306"
	user = "dlaredorazo"
	password = "@Dexsys13"
	databaseString = engineType + user + ":" + password + "@" + host + ":" + port + "/" + db

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


def getComponentReadingClassByType(componentType):
	"""Given the path mapping of a point, get the class that it belongs to"""

	componentClass = None

	if componentType == "AHU":
		componentClass = AHUReading
	elif componentType == "VFD":
		componentClass = VFDReading
	elif componentType == "Filter":
		componentClass = FilterReading
	elif componentType == "Damper":
		componentClass = DamperReading
	elif componentType == "Fan":
		componentClass = FanReading
	elif componentType == "HEC":
		componentClass = HECReading
	elif componentType == "SAV":
		componentClass = SAVReading
	elif componentType == "VAV":
		componentClass = VAVReading
	elif componentType == "Thermafuser":
		componentClass = ThermafuserReading
	else:
		componentClass = None

	return componentClass


def loadData(starTimestamp, endTimestamp, componentTypes = []):
	"""Return a list of dataframes with the data for each of the components in componentTypes in the indicated period"""

	#THIS MUST BE PARALLELIZED ON ORDER TO ACHIEVE ITS MAXIMUM PERFORMANCE

	session = getDBSession()
	readings = dict()
	dataFrames = dict()

	count = 0

	componentsReadingClass = [getComponentReadingClassByType(component) for component in componentTypes]

	#This goes to the log
	print(starTimestamp, endTimestamp, componentsReadingClass)

	#Create the dataframes for each component
	for componentReadingClass in componentsReadingClass:
		readings = \
		session.query(componentReadingClass).filter(and_(componentReadingClass._timestamp >= starTimestamp, componentReadingClass._timestamp < endTimestamp)).all()

		if readings != []:
			#build the dictionary object
			dictionaryOfReadings = copy(readings[0]).__dict__
			dictionaryOfReadings.pop('_sa_instance_state')

			#This is performed fast, no need to change it
			for key in dictionaryOfReadings:
				dictionaryOfReadings[key] = list()

			keys = dictionaryOfReadings.keys()
			
			#Can we make this perform faster?
			for reading in readings:
				readingAsDict = reading.__dict__
				readingAsDict.pop('_sa_instance_state')

				#Can we write a map function (functional programming) for this?
				for key in keys:
					dictionaryOfReadings[key].append(readingAsDict[key])

			dataFrames[componentTypes[count] + 'Readings'] =  pd.DataFrame.from_dict(dictionaryOfReadings)

		count += 1
			
	return dataFrames


def reshapeAndCleanDataFrame(dataFrame, removeSetpoints=False, removeRequests=False, removeBooleans=False):
	"""Reshape the dataframe and return the dataframe reshaped. For each dataframe keep only the data/features that may result useful for the analysis
	for instance it makes no sense to keep boolean values since they are not drawn from a gaussian distribution but instead a binary distribution, 
	and thus they can not be fitted into a gausssian one. Same with setpoints, they are fixed values."""

	#clean dataframe and reshape it
	df = dataFrame

	newColumnNames = {column:column.replace('_', "") for column in df.columns}
	df.rename(columns=newColumnNames, inplace=True)
	
	#Get the Id Column
	idColumn = list(filter(lambda colName: 'Id' in colName or 'Number' in colName, newColumnNames.values()))
	if len(idColumn) != 1:
	    print('Could not determine Id Column')
	else:
	    idColumn = idColumn[0]

	indexColumns = ['timestamp']

	dataColumns = list(filter(lambda colName: idColumn != colName and colName != 'timestamp', newColumnNames.values()))

	#Remove setpoint related columns
	if removeSetpoints == True:
		dropColumns = list(filter(lambda colName: 'setpoint' in colName.lower() or 'stpnt' in colName.lower(), newColumnNames.values()))

	#Remove request related columns
	if removeRequests == True:
		dropColumns += list(filter(lambda colName: "request" in colName.lower() or "req" in colName.lower(), newColumnNames.values()))

	#Remove boolean columns
	if removeBooleans == True:
		dropColumns += list(filter(lambda colName: df[colName].dtype == bool, newColumnNames.values()))

	#drop the undesired columns
	df.drop(dropColumns, axis=1, inplace=True)
	
	df.set_index(indexColumns, inplace=True)
	df.dropna(axis=1, how='all', inplace=True)

	currentColumns = df.columns.values.tolist()

	currentColumns.remove(idColumn)

	#when there is a -1 in the data, replace it by NaN
	df.replace(-1, value=np.nan, inplace=True)
	df.dropna(axis=0, how='all', inplace=True, subset=currentColumns)
	#df.fillna(value=-1)

	#dataFrames[dfkey].fillna(value=nan, inplace=True)

	return df






