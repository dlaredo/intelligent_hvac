from sqlalchemy import Column, Integer, String, Table, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DataPoint(Base):
	"""Class to map to the DataPoints table in the HVAC DB"""

	__tablename__ = 'DataPoints'

	_path = Column('Path', String(255), primary_key = True)
	_server = Column('Server', String(255))
	_location = Column('Location', String(255))
	_branch = Column('Branch', String(255))
	_subBranch = Column('SubBranch', String(255))
	_controlProgram = Column('ControlProgram', String(255))
	_point = Column('Point', String(255))
	_zone = Column('Zone', String(255))

	#Constructor

	def __init__(self, path, server, location, branch, subBranch, controlProgram, point, zone):
		self._path = path
		self._server = server
		self._location = location
		self._branch = branch
		self._subBranch = subBranch
		self._controlProgram = controlProgram
		self._point = point
		self._zone = zone

	#Properties

	@property
	def path(self):
		return self._path

	@path.setter
	def path(self, value):
		self._path = value

	@property
	def server(self):
		return self._server

	@server.setter
	def server(self, value):
		self._server = value

	@property
	def location(self):
		return self._location

	@location.setter
	def location(self, value):
		self._location = value

	@property
	def branch(self):
		return self._branch

	@branch.setter
	def branch(self, value):
		self._branch = value

	@property
	def subBranch(self):
		return self._subBranch

	@subBranch.setter
	def subBranch(self, value):
		self._subBranch = value	

	@property
	def controlProgram(self):
		return self._controlProgram

	@server.setter
	def controlProgram(self, value):
		self._controlProgram = value	

	@property
	def point(self):
		return self._point

	@point.setter
	def point(self, value):
		self._point = value

	@property
	def zone(self):
		return self._zone

	@zone.setter
	def zone(self, value):
		self._zone = value					

	def __str__(self):
		return "<DataPoint(path = '%s', server = '%s', location = '%s', branch = '%s', subBranch = '%s', controlProgram = '%s', point = '%s', zone = '%s')>" \
		% (self._path, self._server, self._location, self._branch, self._subBranch, self._controlProgram, self._point, self._zone)

class AHU(Base):
	"""Class to map to the Air_Handling_Unit table in the HVAC DB"""

	__tablename__ = "Air_Handling_Unit"

	_AHUNumber = Column('AHUNumber', Integer(10), primary_key = True, autoincrement = True)

	#Relationship between AHU and Filter
	_filters = relationship('Filter', back_populates = '_filterNumber')

	#Constructor

	def __init__(self, AHUNumber, filters = None):
		self._AHUNumber = AHUNumber
		self._filters = filters

	#Properties

	@property
	def AHUNumber(self):
		return self._AHUNumber

	@AHUNumber.setter
	def AHUNumber(self, value):
		self._AHUNumber = value

	@property
	def filters(self):
		return self._filters

	@filters.setter
	def filters(self, value):
		self._filters = value

class Filter(Base):
	"""Class to map to the Filter table in the HVAC DB"""

	__tablename__ = "Filter"

	_filterNumber = Column('FilterNumber', String(255), primary_key = True, autoincrement = True)
	_AHUNumber = Column('AHUNumber', Integer(10), ForeingKey("Air_Handling_Unit.AHUNumber"))
	
	#Relatiionship between Filter and AHU
	_ahu = relationship("Air_Handling_Unit", back_populates="_AHUNumber")
	#Relationship between Filter and Filter_Reading
	_filterReadings = relationship("Filter_Reading", back_populates="_filterNumber")

	#Constructor

	def __init__(self, filterNumber, AHUNumber, ahu = None, filterReading = None):
		self._filterNumber = filterNumber
		self._AHUNumber = AHUNumber
		self._ahu = ahu
		self._filterReadings = filterReadings

	#Properties

	@property
	def filterNumber(self):
		return self._filterNumber

	@filterNumber.setter
	def filterNumber(self, value):
		self._filterNumber = value

	@property
	def AHUNumber(self):
		return self._AHUNumber

	@AHUNumber.setter
	def AHUNumber(self, value):
		self._AHUNumber = value

	@property
	def ahu(self):
		return self._ahu

	@ahu.setter
	def ahu(self, value):
		self._ahu = value

	@property
	def filterReadings(self):
		return self._filterReadings

	@filterReadings.setter
	def filterReading(self, value):
		self._filterReadings = value


class FilterReading(Base):
	"""Class to map to the Filter_Reading table in the HVAC DB"""

	__tablename__ = "Filter_Reading"

	_timestamp = Column('Time_Stamp', DateTime, primary_key = True)
	_filterNumber = Column('FilterNumber', Integer(10), primary_key = True, ForeingKey("Filter._filterNumber"))
	_filterType = Column('FilterType', String(255))
	_differencePressure = Column('DifferencePressure', Float(10))
	
	#Relationship between Filter and Filter_Reading
	_filter = relationship("Filter", back_populates="_filterNumber")

	#Constructor

	def __init__(self, timestamp, filterNumber, filterType, differencePressure, filterRef = None):
		self._timestamp = timestamp
		self._filterNumber = filterNumber
		self._filterType = filterType
		self._differencePressure = differencePressure
		self._filter = filterRef

	#Properties

	@property
	def timestamp(self):
		return self._timestamp

	@timestamp.setter
	def timestamp(self, value):
		self._timestamp = value

	@property
	def filterNumber(self):
		return self._filterNumber

	@filterNumber.setter
	def filterNumber(self, value):
		self._filterNumber = value

	@property
	def filterType(self):
		return self._filterType

	@filterType.setter
	def filterType(self, value):
		self._filterType = value

	@property
	def differencePressure(self):
		return self._differencePressure

	@differencePressure.setter
	def differencePressure(self, value):
		self._differencePressure = value

	@property
	def filter(self):
		return self._filter

	@filter.setter
	def filter(self, value):
		self._filter = value

