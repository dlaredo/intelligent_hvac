from sqlalchemy import Column, Integer, String, Table, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import PrimaryKeyConstraint
import csv
import sqlalchemy
from hvacDBMapping import *
from sqlalchemy.orm import sessionmaker
import traceback
from datetime import datetime
import re
import os
from dateutil.parser import *
import copy
from sqlalchemy.inspection import inspect
from sqlalchemy.orm.util import identity_key

Base = declarative_base()


class ThermafuserReading(Base):
	"""Class to map to the Thermafuser Readings table in the HVAC DB"""

	__tablename__ = 'Thermafuser_Reading'

	_timestamp = Column('Time_stamp', DateTime, primary_key = True)
	_thermafuserId = Column('ThermafuserId', Integer, ForeignKey("Thermafuser.ThermafuserId"), primary_key = True)

	#Constructor

	def __init__(self, timestamp, thermafuserId):

		self._thermafuserId = thermafuserId
		self._timestamp = timestamp

	#properties

	@property
	def thermafuserId(self):
		return self._thermafuserId

	@thermafuserId.setter
	def thermafuserId(self, value):
		self._thermafuserId = value

	@property
	def timestamp(self):
		return self._timestamp

	@timestamp.setter
	def timestamp(self, value):
		self._timestamp = value

	def __str__(self):
		return "<ThermafuserReading(thermafuserId = '%s', timestamp = '%s')>" % (self._thermafuserId, str(self._timestamp))


def main():

	Session = sessionmaker()
	session = Session() 

	mapper = inspect(ThermafuserReading)

	#Open the csv file
	csvFilePath = "/Users/davidlaredorazo/Box Sync/Data/Zone4/1C1A/1C1A 2016-12-31.csv"
	with open(csvFilePath, 'r') as csvfile:

		reader = csv.reader(csvfile)
		componentId = 1
		count = 0

		reading = ThermafuserReading(None, componentId)

		for row in reader:

			if count == 0:
				count += 1
				continue

			#print(row)
			timestamp = parse(row[0], None, ignoretz = True)

			reading.timestamp = timestamp
			new_object = copy.copy(reading)
			new_object.timestamp = timestamp

			#print(new_object, mapper.identity_key_from_instance(new_object))
			session.add(new_object)

	print("new elements")
	for new in session.new:
		print(new)

main()














