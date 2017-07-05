from sqlalchemy import Column, Integer, String, Table, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

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
	_zone = Column('Zone', Integer)
	_componentId = Column('ComponentId', Integer)
	_pathMappingId = Column('PathMappingsId', Integer, ForeignKey("PathMappings.Id"))

	#PathMapping relationship
	_pathMapping = relationship("PathMapping", back_populates = "_dataPoints")

	#Constructor

	def __init__(self, path, server, location, branch, subBranch, controlProgram, point, zone, componentId = None, pathMappingId = None, pathMapping = None):

		self._path = path
		self._server = server
		self._location = location
		self._branch = branch
		self._subBranch = subBranch
		self._controlProgram = controlProgram
		self._point = point
		self._zone = zone
		self._componentId = componentId
		self._pathMappingId = pathMappingId
		self._pathMapping = pathMapping

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

	@controlProgram.setter
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

	@property
	def componentId(self):
		return self._componentId

	@componentId.setter
	def componentId(self, value):
		self._componentId = value 

	@property
	def pathMappingId(self):
		return self._pathMappingId

	@pathMappingId.setter
	def pathMappingId(self, value):
		self._pathMappingId = value 

	@property
	def pathMapping(self):
		return self._pathMapping

	@pathMapping.setter
	def pathMapping(self, value):
		self._pathMapping = value                 

	def __str__(self):
		return "<DataPoint(path = '%s', server = '%s', location = '%s', branch = '%s', subBranch = '%s', controlProgram = '%s', point = '%s',\
		 zone = '%s', componentId = '%s', pathMappingId = '%s', pathMapping = '%s')>" \
		% (self._path, self._server, self._location, self._branch, self._subBranch, self._controlProgram, self._point,\
		 self._zone, self._componentId, self._pathMappingId, str(self._pathMapping))


class PathMapping(Base):
	"""Class to map to the DataPoints table in the HVAC DB"""

	__tablename__ = 'PathMappings'

	_id = Column('Id', Integer, primary_key = True)
	_path = Column('Path', String(255))
	_componentType = Column('ComponentType', String(255))
	_description = Column('Description', String(255))
	_databaseMapping = Column('DatabaseMapping', String(255))

	#PathMapping relationship
	_dataPoints = relationship("DataPoint", back_populates = "_pathMapping")

	#Constructor

	def __init__(self, identifier, path, componentType, description, databaseMapping, dataPoints = []):

		self._id = identifier
		self._path = path
		self._componentType = componentType
		self._description = description
		self._databaseMapping = databaseMapping
		self._dataPoints = dataPoints

	#Properties

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, value):
		self._id = value

	@property
	def path(self):
		return self._path

	@path.setter
	def path(self, value):
		self._path = value

	@property
	def componentType(self):
		return self._componentType

	@componentType.setter
	def componentType(self, value):
		self._componentType = value

	@property
	def description(self):
		return self._description

	@description.setter
	def description(self, value):
		self._description = value

	@property
	def databaseMapping(self):
		return self._databaseMapping

	@databaseMapping.setter
	def databaseMapping(self, value):
		self._databaseMapping = value

	@property
	def dataPoints(self):
		return self._dataPoints

	@dataPoints.setter
	def dataPoints(self, value):
		self._dataPoints = value  

	def __str__(self):
		return "<DataPoint(id = '%s', path = '%s', componentType = '%s', description = '%s', databaseMapping = '%s', dataPoints = '%s')>" \
		% (self._id, self._path, self._componentType, self._description, self._databaseMapping, str(self._dataPoints))


class ComponentRelationship(Base):
	"""Class to map to the DataPoints table in the HVAC DB"""

	__tablename__ = 'ComponentRelationships'

	_componentName = Column('ComponentName', String(255), primary_key = True)
	_parentComponent = Column('ParentComponent', String(255), ForeignKey("ComponentRelationships.ComponentName"))
	_componentType = Column('ComponentType', String(255))
	_group = Column('ComponentGroup', String(255))

	#Relationships between Component parents and children
	#_parent = relationship("ComponentRelationship", back_populates = "_children")
	_children = relationship("ComponentRelationship", backref = backref('_parent', remote_side=[_componentName]))

	#Constructor

	def __init__(self, componentName, parentComponent, componentType, group, parent = None, children = []):

		self._componentName = componentName
		self._parentComponent = parentComponent
		self._componentType = componentType
		self._group = group
		self._parent = parent
		self._children = children

	#Properties

	@property
	def componentName(self):
		return self._componentName

	@componentName.setter
	def componentName(self, value):
		self._componentName = value

	@property
	def parentComponent(self):
		return self._parentComponent

	@parentComponent.setter
	def parentComponent(self, value):
		self._parentComponent = value

	@property
	def componentType(self):
		return self._componentType

	@componentType.setter
	def componentType(self, value):
		self._componentType = value

	@property
	def group(self):
		return self._group

	@group.setter
	def group(self, value):
		self._group = value 

	@property
	def parent(self):
		return self._parent

	@parent.setter
	def parent(self, value):
		self._parent = value 

	@property
	def children(self):
		return self._children

	@children.setter
	def children(self, value):
		self._children = value 

	def __str__(self):
		return "<DataPoint(componentName = '%s', parentComponent = '%s', componentType = '%s', group = '%s', parent = '%s', children = '%s')>" %\
		 (self._componentName, self._parentComponent, self._componentType, self._group, str(self._parent), str(self._children))


class AHU(Base):
	"""Class to map to the Air_Handling_Unit table in the HVAC DB"""

	__tablename__ = "Air_Handling_Unit"

	_AHUNumber = Column('AHUNumber', Integer, primary_key = True, autoincrement = True)
	_AHUName = Column('AHUName', String(255))

	#Relationships

	_ahuReadings = relationship('AHUReading', back_populates = '_ahu') #AHUReadings and AHU
	_filters = relationship('Filter', back_populates = '_ahu') #Filter and AHU
	_fans = relationship('Fan', back_populates = '_ahu') #Fan and AHU
	_dampers = relationship('Damper', back_populates = '_ahu') #Damper and AHU
	_vavs = relationship('VAV', back_populates = '_ahu') #VAV and AHU
	_savs = relationship('SAV', back_populates = '_ahu') #SAV and AHU
	_hecs = relationship('HEC', back_populates = '_ahu') #HEC and AHU
	_vfds = relationship('VFD', back_populates = '_ahu') #VFD and AHU
	_thermafusers = relationship('Thermafuser', back_populates = '_ahu') #Thermafuser and AHU

	#Constructor

	def __init__(self, AHUNumber, AHUName, ahuReadings = [], filters = [], fans = [], dampers = [], vavs = [], savs = [], hecs = [], vfds = [], thermafusers = []):

		self._AHUNumber = AHUNumber
		self._AHUName = AHUName
		self._ahuReadings = ahuReadings
		self._filters = filters
		self._fans = fans
		self._dampers = dampers
		self._vavs = vavs
		self._savs = savs
		self._hecs = hecs
		self._vfds = vfds
		self._thermafusers = thermafusers

	#Properties

	@property
	def AHUNumber(self):
		return self._AHUNumber

	@AHUNumber.setter
	def AHUNumber(self, value):
		self._AHUNumber = value

	@property
	def AHUName(self):
		return self._AHUName

	@AHUName.setter
	def AHUName(self, value):
		self._AHUName = value

	@property
	def ahuReadings(self):
		return self._ahuReadings

	@ahuReadings.setter
	def ahuReadings(self, value):
		self._ahuReadings = value

	@property
	def filters(self):
		return self._filters

	@filters.setter
	def filters(self, value):
		self._filters = value

	@property
	def fans(self):
		return self._fans

	@fans.setter
	def fans(self, value):
		self._fans = value

	@property
	def dampers(self):
		return self._dampers

	@dampers.setter
	def dampers(self, value):
		self._dampers = value

	@property
	def vavs(self):
		return self._vavs

	@vavs.setter
	def vavs(self, value):
		self._vavs = value

	@property
	def savs(self):
		return self._savs

	@savs.setter
	def savs(self, value):
		self._savs = value

	@property
	def hecs(self):
		return self._hecs

	@hecs.setter
	def hecs(self, value):
		self._hecs = value

	@property
	def vfds(self):
		return self._vfds

	@vfds.setter
	def vfds(self, value):
		self._vfds = value

	@property
	def thermafusers(self):
		return self._thermafusers

	@thermafusers.setter
	def thermafusers(self, value):
		self._thermafusers = value

	#Methods

	def getComponentName(self):
		return self._AHUName

	def getComponentType(self):
		return "AHU"

	def __str__(self):
		return "<AHU(AHUNumber = '%d', AHUName = '%s', ahuReadings = '%s', filters = '%s', fans = '%s', dampers = '%s', vavs = '%s', savs = '%s', hecs = '%s', vfds = '%s', thermafusers = '%s' )>" \
		% (self._AHUNumber, self._AHUName, str(self._ahuReadings), str(self._filters), str(self._fans), str(self._dampers), str(self._vavs), str(self._savs), str(self._hecs), str(self._vfds),\
		 str(self._thermafusers))


class AHUReading(Base):
	"""Class to map to the Air Handling Unit Readings table in the HVAC DB"""

	__tablename__ = 'Air_Handling_Unit_Reading'

	_AHUNumber = Column('AHUNumber', String(255), ForeignKey("Air_Handling_Unit.AHUNumber"), primary_key = True)
	_time_stamp = Column('Time_stamp', String(255), primary_key = True)
	_zoneTemperature = Column('ZoneTemperature', Float)
	_staticPressure = Column('StaticPressure', Float)
	_returnAirTemperature = Column('ReturnAirTemperature', Float, nullable=True)
	_supplyAirTemperature = Column('SupplyAirTemperature', Float, nullable=True)
	_exhaustAirTemperature = Column('ExhaustAirTemperature', Float, nullable=True)
	_outsideAirTemperature = Column('OutsideAirTemperature', Float, nullable=True)
	_smokeDetector = Column('SmokeDetector', Boolean, nullable=True)
	_outsideAirCo2 = Column('OutsideAirCO2', Float, nullable=True)
	_returnAirCo2 = Column('ReturnAirCO2', Float, nullable=True)
	_spare = Column('Spare', Float, nullable=True)
	_hiStatic = Column('HiStatic', Boolean, nullable=True)
	_ductStaticPressure = Column('DuctStaticPressure', Float, nullable=True)
	_mixedAirTemperature = Column('MixedAirTemperature', Float, nullable=True)        
	_OSACFM = Column('OutsideAirCFM', Float, nullable=True)
	_coolingRequest = Column('CoolingRequest', Float, nullable=True)
	_coolingSetpoint = Column('CoolingSetpoint', Float, nullable=True)
	_heatingRequest = Column('HeatingRequest', Float, nullable=True)
	_heatingSetpoint = Column('HeatingSetpoint', Float, nullable=True)
	_economizerSetpoint = Column('EconomizerSetpoint', Float, nullable=True)
	_occupiedMode = Column('OccupiedMode', Boolean, nullable=True)
	_returnAirCo2Setpoint = Column('ReturnAirCO2Setpoint', Float, nullable=True)
	_staticPressureSmoothed = Column('StaticPressureSmoothed', Float, nullable=True)
	_staticSP = Column('StaticSP', Float, nullable=True)

	#Relationship between AHU Reading and AHU
	_ahu = relationship("AHU", back_populates = "_ahuReadings")

	#Constructor

	def __init__(self, AHUNumber, Time_stamp, zoneTemperature = None, staticPressure = None, returnAirTemperature = None, supplyAirTemperature = None, exhaustAirTemperature = None,\
	 outsideAirTemperature = None, smokeDetector = None, outsideAirCo2 = None, returnAirCo2 = None, spare = None, hiStatic = None, ductstaticPressure = None,\
	  mixedAirTemperature = None, OSACFM = None, coolingRequest = None, coolingSetpoint = None, heatingRequest = None, heatingSetpoint = None, economizerSetpoint = None,\
	  occupiedMode = None, returnAirCo2Setpoint = None, staticPressureSmoothed = None, staticSP = None, ahu = None):

		self._AHUNumber = AHUNumber
		self._time_stamp = Time_stamp
		self._zoneTemperature = zoneTemperature
		self._staticPressure = staticPressure
		self._returnAirTemperature = returnAirTemperature
		self._supplyAirTemperature = supplyAirTemperature
		self._exhaustAirTemperature = exhaustAirTemperature
		self._outsideAirTemperature = outsideAirTemperature                
		self._smokeDetector = smokeDetector
		self._outsideAirCo2 = outsideAirCo2
		self._returnAirCo2 = returnAirCo2
		self._spare = spare
		self._hiStatic = hiStatic
		self._ductStaticPressure = ductStaticPressure
		self._mixedAirTemperature = mixedAirTemperature                
		self._OSACFM = OSACFM

		self._coolingRequest = coolingRequest
		self._coolingSetpoint = coolingSetpoint
		self._heatingRequest = heatingRequest
		self._heatingSetpoint = heatingSetpoint
		self._economizerSetpoint = economizerSetpoint
		self._occupiedMode = occupiedMode
		self._returnAirCo2Setpoint = returnAirCo2Setpoint
		self._staticPressureSmoothed = staticPressureSmoothed
		self._staticSP = staticSP

		self._ahu = ahu

	#properties

	@property
	def AHUNumber(self):
		return self._AHUNumber

	@AHUNumber.setter
	def AHUNumber(self, value):
		self._AHUNumber = value

	@property
	def time_stamp(self):
		return self._time_stamp

	@time_stamp.setter
	def time_stamp(self, value):
		self._time_stamp = value

	@property
	def zoneTemperature(self):
		return self._zoneTemperature

	@zoneTemperature.setter
	def zoneTemperature(self, value):
		self._zoneTemperature = value

	@property
	def staticPressure(self):
		return self._staticPressure

	@staticPressure.setter
	def staticPressure(self, value):
		self._staticPressure = value

	@property
	def returnAirTemperature(self):
		return self._returnAirTemperature

	@returnAirTemperature.setter
	def returnAirTemperature(self, value):
		self._returnAirTemperature = value  

	@property
	def supplyAirTemperature(self):
		return self._supplyAirTemperature

	@supplyAirTemperature.setter
	def supplyAirTemperature(self, value):
		self._supplyAirTemperature = value  

	@property
	def exhaustAirTemperature(self):
		return self._exhaustAirTemperature

	@exhaustAirTemperature.setter
	def exhaustAirTemperature(self, value):
		self._exhaustAirTemperature = value 
	@property
	def outsideAirTemperature(self):
		return self._outsideAirTemperature

	@outsideAirTemperature.setter
	def outsideAirTemperature(self, value):
		self._outsideAirTemperature = value 
		
	@property
	def smokeDetector(self):
		return self._smokeDetector

	@smokeDetector.setter
	def smokeDetector(self, value):
		self._smokeDetector = value 
		
	@property
	def outsideAirCo2(self):
		return self._outsideAirCo2

	@outsideAirCo2.setter
	def outsideAirCo2(self, value):
		self._outsideAirCo2 = value 
		
	@property
	def returnAirCo2(self):
		return self._returnAirCo2

	@returnAirCo2.setter
	def returnAirCo2(self, value):
		self._returnAirCo2 = value
		
	@property
	def spare(self):
		return self._spare

	@spare.setter
	def spare(self, value):
		self._spare = value 
	
	@property
	def hiStatic(self):
		return self._hiStatic

	@hiStatic.setter
	def hiStatic(self, value):
		self._hiStatic = value  
	
	@property
	def ductStaticPressure(self):
		return self._ductStaticPressure

	@ductStaticPressure.setter
	def ductStaticPressure(self, value):
		self._ductStaticPressure = value    
	
	@property
	def mixedAirTemperature(self):
		return self._mixedAirTemperature

	@mixedAirTemperature.setter
	def mixedAirTemperature(self, value):
		self._mixedAirTemperature = value   
	
	@property
	def OSACFM(self):
		return self._OSACFM

	@OSACFM.setter
	def OSACFM(self, value):
		self._OSACFM = value

	@property
	def coolingRequest(self):
		return self._coolingRequest

	@coolingRequest.setter
	def coolingRequest(self, value):
		self._coolingRequest = value

	@property
	def coolingSetpoint(self):
		return self._coolingSetpoint

	@coolingSetpoint.setter
	def coolingSetpoint(self, value):
		self._coolingSetpoint = value
	
	@property
	def heatingRequest(self):
		return self._heatingRequest

	@heatingRequest.setter
	def heatingRequest(self, value):
		self._heatingRequest = value

	@property
	def heatingSetpoint(self):
		return self._heatingSetpoint

	@heatingSetpoint.setter
	def heatingSetpoint(self, value):
		self._heatingSetpoint = value
	
	@property
	def economizerSetpoint(self):
		return self._economizerSetpoint

	@economizerSetpoint.setter
	def economizerSetpoint(self, value):
		self._economizerSetpoint = value
	
	@property
	def occupiedMode(self):
		return self._occupiedMode

	@occupiedMode.setter
	def occupiedMode(self, value):
		self._occupiedMode = value
	
	@property
	def returnAirCo2Setpoint(self):
		return self._returnAirCo2Setpoint

	@returnAirCo2Setpoint.setter
	def returnAirCo2Setpoint(self, value):
		self._returnAirCo2Setpoint = value
	
	@property
	def staticPressureSmoothed(self):
		return self._staticPressureSmoothed

	@staticPressureSmoothed.setter
	def staticPressureSmoothed(self, value):
		self._staticPressureSmoothed = value
	
	@property
	def staticSP(self):
		return self._staticSP

	@staticSP.setter
	def staticSP(self, value):
		self._staticSP = value

	@property
	def ahu(self):
		return self._ahu

	@ahu.setter
	def ahu(self, value):
		self._ahu = value

	def __str__(self):
		return "<AHUReading(AHUNumber = '%s', Time_stamp = '%s', zoneTemperature = '%s', staticPressure = '%s', returnAirTemperature = '%s', supplyAirTemperature = '%s', \
		exhaustAirTemperature = '%s', outsideAirTemperature = '%s',smokeDetector = '%s',outsideAirCo2 = '%s', returnAirCo2 = '%s',spare = '%s',hiStatic = '%s', \
		ductstaticPressure = '%s',mixedAirTemperature = '%s', OSACFM = '%s', CoolingRequest = '%s', CoolingSetpoint = '%s', HeatingRequest = '%s', HeatingSetpoint = '%s',\
		EconomizerSetpoint = '%s', OccupiedMode = '%s', ReturnAirCo2Setpoint = '%s', StaticPressureSmoothed = '%s', StaticSP = '%s', ahu = '%s')>" \
		% (self._AHUNumber, self._Time_stamp, self._zoneTemperature, self._staticPressure, self._returnAirTemperature, self._supplyAirTemperature, \
		 self._exhaustAirTemperature, self._outsideAirTemperature,self._smokeDetector,self._outsideAirCo2,self._returnAirCo2, self._spare, self._hiStatic, \
		 self._ductstaticPressure, self._mixedAirTemperature, self._OSACFM, self._coolingRequest, self._coolingSetpoint, self._heatingRequest, self._heatingSetpoint,\
		 self._economizerSetpoint, self._occupiedMode, self._returnAirCo2Setpoint, self._staticPressureSmoothed, self._staticSP, str(self._ahu))


class VFD(Base):
	"""Class to map to the Filter table in the HVAC DB"""

	__tablename__ = "VFD"

	_vfdId = Column('VFDId', Integer, primary_key = True, autoincrement = True)
	_AHUNumber = Column('AHUNumber', Integer, ForeignKey("Air_Handling_Unit.AHUNumber"))
	_vfdName = Column('VFDName', String(255))
	_vfdType = Column('VFDType', String(255))
	
	#Relationships
	_ahu = relationship("AHU", back_populates = "_vfds") #Relatiionship between Filter and AHU
	_vfdReadings = relationship("VFDReading", back_populates = "_vfd") #Relationship between Filter and Filter_Reading

	#Constructor

	def __init__(self, vfdId, AHUNumber, vfdName, vfdType, ahu = None, vfdReadings = []):

		self._vfdId = vfdId
		self._vfdName = vfdName
		self._AHUNumber = AHUNumber
		self._vfdType = vfdType
		self._ahu = ahu
		self._vfdReadings = vfdReadings

	#Properties

	@property
	def vfdId(self):
		return self._vfdId

	@vfdId.setter
	def vfdId(self, value):
		self._vfdId = value

	@property
	def vfdName(self):
		return self._vfdName

	@vfdName.setter
	def vfdName(self, value):
		self._vfdName = value

	@property
	def AHUNumber(self):
		return self._AHUNumber

	@AHUNumber.setter
	def AHUNumber(self, value):
		self._AHUNumber = value

	@property
	def vfdType(self):
		return self._vfdType

	@vfdType.setter
	def vfdType(self, value):
		self._vfdType = value

	@property
	def ahu(self):
		return self._ahu

	@ahu.setter
	def ahu(self, value):
		self._ahu = value

	@property
	def vfdReadings(self):
		return self._vfdReadings

	@vfdReadings.setter
	def vfdReadings(self, value):
		self._vfdReadings = value

	#Methods

	def getComponentName(self):
		return self._vfdName

	def getComponentType(self):
		return "VFD" + self._vfdType

	def __str__(self):
		return "<Filter(vfdId = '%d', AHUNumber = '%d', vfdName = '%d',  vfdType = '%s', ahu = '%s', vfdReadings = '%s')>" \
		% (self._vfdId, self._AHUNumber, self._vfdName, self._vfdType, str(self._ahu), str(self._vfdReadings))


class VFDReading(Base):
	"""Class to map to the Filter_Reading table in the HVAC DB"""

	__tablename__ = "VFD_Reading"

	_timestamp = Column('Time_Stamp', DateTime, primary_key = True)
	_vfdId = Column('VFDId', Integer, ForeignKey("VFD.VFDId"), primary_key = True)
	_powerKW = Column('PowerKW', Float)
	_speedRPM = Column('SpeedRPM', Float)
	
	#Relationship between Filter and Filter_Reading
	_vfd = relationship("VFD", back_populates = "_vfdReadings")

	#Constructor

	def __init__(self, timestamp, vfdId, powerKW = None, speedRPM = None, vfdRef = None):

		self._timestamp = timestamp
		self._vfdId = vfdId
		self._powerKW = powerKW
		self._speedRPM = speedRPM
		self._vfd = vfdRef

	#Properties

	@property
	def timestamp(self):
		return self._timestamp

	@timestamp.setter
	def timestamp(self, value):
		self._timestamp = value

	@property
	def vfdId(self):
		return self._vfdId

	@vfdId.setter
	def vfdId(self, value):
		self._vfdId = value

	@property
	def powerKW(self):
		return self._powerKW

	@powerKW.setter
	def powerKW(self, value):
		self._powerKW = value

	@property
	def speedRPM(self):
		return self._speedRPM

	@speedRPM.setter
	def speedRPM(self, value):
		self._speedRPM = value

	@property
	def vfd(self):
		return self._vfd

	@vfd.setter
	def vfd(self, value):
		self._vfd = value

	def __str__(self):
		return "<FilterReading(timestamp = '%s', vfdId = '%s', powerKW = '%s', speedRPM = '%s', vfd = '%s')>" \
		% (str(self._timestamp), self._vfdId, self._powerKW, self._speedRPM, str(self._vfd))


class Filter(Base):
	"""Class to map to the Filter table in the HVAC DB"""

	__tablename__ = "Filter"

	_filterId = Column('FilterId', Integer, primary_key = True, autoincrement = True)
	_AHUNumber = Column('AHUNumber', Integer, ForeignKey("Air_Handling_Unit.AHUNumber"))
	_filterName = Column('FilterName', String(255))
	_filterType = Column('FilterType', String(255))
	
	#Relationships
	_ahu = relationship("AHU", back_populates = "_filters") #Relatiionship between Filter and AHU
	_filterReadings = relationship("FilterReading", back_populates = "_filter") #Relationship between Filter and Filter_Reading

	#Constructor

	def __init__(self, filterId, AHUNumber, filterName, filterType = None, ahu = None, filterReadings = []):

		self._filterId = filterId
		self._filterName = filterName
		self._AHUNumber = AHUNumber
		self._filterType = filterType
		self._ahu = ahu
		self._filterReadings = filterReadings

	#Properties

	@property
	def filterId(self):
		return self._filterId

	@filterId.setter
	def filterId(self, value):
		self._filterId = value

	@property
	def filterName(self):
		return self._filterName

	@filterName.setter
	def filterName(self, value):
		self._filterName = value

	@property
	def AHUNumber(self):
		return self._AHUNumber

	@AHUNumber.setter
	def AHUNumber(self, value):
		self._AHUNumber = value

	@property
	def filterType(self):
		return self._filterType

	@filterType.setter
	def filterType(self, value):
		self._filterType = value

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
	def filterReadings(self, value):
		self._filterReadings = value

	#Methods

	def getComponentName(self):
		return self._filterName

	def getComponentType(self):
		return "Filter" + self._filterType

	def __str__(self):
		return "<Filter(filterId = '%d', AHUNumber = '%d', filterName = '%d', filterType = '%s', ahu = '%s', filterReadings = '%s')>" \
		% (self._filterId, self._AHUNumber, self._filterName, self._filterType, str(self._ahu), str(self._filterReadings))


class FilterReading(Base):
	"""Class to map to the Filter_Reading table in the HVAC DB"""

	__tablename__ = "Filter_Reading"

	_timestamp = Column('Time_Stamp', DateTime, primary_key = True)
	_filterId = Column('FilterId', Integer, ForeignKey("Filter.FilterId"), primary_key = True)
	_differencePressure = Column('DifferencePressure', Float)
	
	#Relationship between Filter and Filter_Reading
	_filter = relationship("Filter", back_populates = "_filterReadings")

	#Constructor

	def __init__(self, timestamp, filterId, differencePressure = None, filterRef = None):

		self._timestamp = timestamp
		self._filterId = filterId
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
	def filterId(self):
		return self._filterId

	@filterId.setter
	def filterId(self, value):
		self._filterId = value

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

	def __str__(self):
		return "<FilterReading(timestamp = '%s', filterId = '%s', differencePressure = '%s', filter = '%s')>" \
		% (str(self._timestamp), self._filterId, self._differencePressure, str(self._filter))


class Damper(Base):
	"""Class to map to the Damper table in the HVAC DB"""

	__tablename__ = "Damper"

	_damperId = Column('DamperId', Integer, primary_key = True, autoincrement = True)
	_AHUNumber = Column('AHUNumber', Integer, ForeignKey("Air_Handling_Unit.AHUNumber"))
	_damperName = Column('DamperName', String(255))
	_damperType = Column('DamperType', String(255))
	
	#Relationships

	_ahu = relationship("AHU", back_populates = "_dampers") #Relatiionship between Damper and AHU
	_damperReadings = relationship("DamperReading", back_populates = "_damper") #Relationship between Damper and Damper_Reading

	#Constructor

	def __init__(self, damperId, AHUNumber, damperName, damperType = None, ahu = None, damperReadings = []):

		self._damperId = damperId
		self._AHUNumber = AHUNumber
		self._damperName = damperName
		self._damperType = damperType
		self._ahu = ahu
		self._damperReadings = damperReadings

	#Properties

	@property
	def damperId(self):
		return self._damperId

	@damperId.setter
	def damperId(self, value):
		self._damperId = value

	@property
	def damperName(self):
		return self._damperName

	@damperName.setter
	def damperName(self, value):
		self._damperName = value

	@property
	def AHUNumber(self):
		return self._AHUNumber

	@AHUNumber.setter
	def AHUNumber(self, value):
		self._AHUNumber = value

	@property
	def damperType(self):
		return self._damperType

	@damperType.setter
	def damperType(self, value):
		self._damperType = value

	@property
	def ahu(self):
		return self._ahu

	@ahu.setter
	def ahu(self, value):
		self._ahu = value

	@property
	def damperReadings(self):
		return self._damperReadings

	@damperReadings.setter
	def damperReadings(self, value):
		self._damperReadings = value

	#Methods

	def getComponentName(self):
		return self._damperName

	def getComponentType(self):
		return "Damper" + self._damperType

	def __str__(self):
		return "<Damper(damperId = '%d', AHUNumber = '%d', damperName = '%d', damperType = '%s', ahu = '%s', damperReadings = '%s')>" \
		% (self._damperId, self._AHUNumber, self._damperName, self._damperType, str(self._ahu), str(self._damperReadings))


class DamperReading(Base):
	"""Class to map to the Damper_Reading table in the HVAC DB"""

	__tablename__ = 'Damper_Reading'

	_damperId = Column('DamperId', Integer, ForeignKey("Damper.DamperId"), primary_key = True)
	_time_stamp = Column('Time_stamp', DateTime, primary_key=True)
	_damperInputVoltage = Column('DamperInputVoltage', Float, nullable=True)
	_damperOpeningPercentage = Column('DamperOpeningPercentage', Float, nullable=True)
	_isolationDamper = Column('isolationDamper', Boolean, nullable=True )

	#Relationship between Damper and Damper_Reading
	_damper = relationship("Damper", back_populates = "_damperReadings")

	#Constructor

	def __init__(self, damperId, time_stamp, damperInputVoltage = None, damperOpeningPercentage = None, isolationDamper = None, damper = None):

		self._damperId = damperId
		self._time_stamp = time_stamp
		self._damperInputVoltage = damperInputVoltage
		self._damperOpeningPercentage = damperOpeningPercentage
		self._isolationDamper = isolationDamper
		self._damper = damper

	#properties

	@property
	def damperId(self):
		return self._damperId

	@damperId.setter
	def damperId(self, value):
		self._damperId = value

	@property
	def time_stamp(self):
		return self._time_stamp

	@time_stamp.setter
	def time_stamp(self, value):
		self._time_stamp = value

	@property
	def damperInputVoltage(self):
		return self.damperInputVoltage

	@damperInputVoltage.setter
	def damperInputVoltage(self, value):
		self._damperInputVoltage = value

	@property
	def damperOpeningPercentage(self):
		return self._damperOpeningPercentage

	@damperOpeningPercentage.setter
	def damperOpeningPercentage(self, value):
		self._damperOpeningPercentage = value   

	@property
	def isolationDamper(self):
		return self._isolationDamper

	@isolationDamper.setter
	def isolationDamper(self, value):
		self._isolationDamper= value

	@property
	def damper(self):
		return self._damper

	@damper.setter
	def damper(self, value):
		self._damper = value            

	def __str__(self):
		return "<DamperReading(damperId = '%s', time_stamp = '%s', damperInputVoltage = '%s', damperOpeningPercentage = '%s', isolationDamper = '%s', damper = '%s')>" \
		% (self._damperId, self._time_stamp, self._damperInputVoltage, self._damperOpeningPercentage, self._isolationDamper, str(self._damper))


class Fan(Base):
	"""Class to map to the Fan table in the HVAC DB"""

	__tablename__ = "Fan"

	_fanId = Column('FanId', Integer, primary_key = True, autoincrement = True)
	_AHUNumber = Column('AHUNumber', Integer, ForeignKey("Air_Handling_Unit.AHUNumber"))
	_fanName = Column('FanName', String(255))
	_fanType = Column('FanType', String(255))
	
	#Relationships

	_ahu = relationship("AHU", back_populates = "_fans") #Relationship between Fan and AHU
	_fanReadings = relationship("FanReading", back_populates = "_fan") #Relationship between Fan and Fan_Reading

	#Constructor

	def __init__(self, fanId, AHUNumber, fanName, fanType = None, ahu = None, fanReadings = []):

		self._fanId = fanId
		self._AHUNumber = AHUNumber
		self._fanName = fanName
		self._fanType = fanType
		self._ahu = ahu
		self._fanReadings = fanReadings

	#Properties

	@property
	def fanId(self):
		return self._fanId

	@fanId.setter
	def fanId(self, value):
		self._fanId = value

	@property
	def fanName(self):
		return self._fanName

	@fanName.setter
	def fanName(self, value):
		self._fanName = value

	@property
	def AHUNumber(self):
		return self._AHUNumber

	@AHUNumber.setter
	def AHUNumber(self, value):
		self._AHUNumber = value

	@property
	def fanType(self):
		return self._fanType

	@fanType.setter
	def fanType(self, value):
		self._fanType = value

	@property
	def ahu(self):
		return self._ahu

	@ahu.setter
	def ahu(self, value):
		self._ahu = value

	@property
	def fanReadings(self):
		return self._fanReadings

	@fanReadings.setter
	def fanReadings(self, value):
		self._fanReadings = value

	#Methods

	def getComponentName(self):
		return self._fanName

	def getComponentType(self):
		return "Fan" + self._fanType

	def __str__(self):
		return "<Fan(fanId = '%d', AHUNumber = '%d', fanName = '%d', fanType = '%s', ahu = '%s', fanReadings = '%s')>" \
		% (self._fanId, self._AHUNumber, self._fanName, self._fanType, str(self._ahu), str(self._fanReadings))


class FanReading(Base):
	"""Class to map to the Fan Reading table in the HVAC DB"""

	__tablename__ = 'Fan_Reading'

	_fanId = Column('FanId', Integer, ForeignKey("Fan.FanId"), primary_key = True)
	_time_stamp = Column('Time_stamp', DateTime, primary_key = True)
	_airVelocityPressure = Column('AirVelocityPressure', Float, nullable=True)
	_VFDSpeed = Column('VFDSpeed', Float, nullable=True)
	_fanStatus = Column('FanStatus', Boolean, nullable=True)
	_VFDFault = Column('VFDFault', Boolean, nullable=True)
	_HiStaticReset = Column('HiStaticReset', Boolean, nullable=True)
	_FAReturnFanShutdown = Column('FAReturnFanShutdown', Boolean, nullable=True)
	_fanVFD = Column('FanVFD', Boolean, nullable=True)
	_isolationDampers = Column('IsolationDampers', Boolean, nullable=True)
	_fanSS = Column('FanSS', Boolean, nullable=True)
	_airVelocityCFM = Column('AirVelocityCFM', Float, nullable=True)

	#Relationship between Fan and Fan_Reading
	_fan = relationship("Fan", back_populates = "_fanReadings")

	#Constructor

	def __init__(self, fanId, time_stamp, airVelocityPressure = None, VFDSpeed = None, fanStatus = None, VFDFault = None, HiStaticReset = None,\
	 FAReturnFanShutdown = None, fanVFD = None, isolationDampers = None, fanSS = None, airVelocityCFM = None, fan = None):

		self._fanId = fanId
		self._time_stamp = time_stamp
		self._airVelocityPressure = airVelocityPressure
		self._VFDSpeed = VFDSpeed
		self._fanStatus = fanStatus
		self._VFDFault = VFDFault
		self._HiStaticReset = HiStaticReset
		self._FAReturnFanShutdown = FAReturnFanShutdown                
		self._fanVFD = fanVFD
		self._isolationDampers = isolationDampers
		self._fanSS = fanSS
		self._airVelocityCFM = airVelocityCFM
		self._fan = fan

	#properties

	@property
	def fanId(self):
		return self._fanId

	@fanId.setter
	def fanId(self, value):
		self._fanId = value

	@property
	def time_stamp(self):
		return self._time_stamp

	@time_stamp.setter
	def time_stamp(self, value):
		self._time_stamp = value

	@property
	def airVelocityPressure(self):
		return self._airVelocityPressure

	@airVelocityPressure.setter
	def airVelocityPressure(self, value):
		self._airVelocityPressure = value

	@property
	def VFDSpeed(self):
		return self._VFDSpeed

	@VFDSpeed.setter
	def VFDSpeed(self, value):
		self._VFDSpeed = value

	@property
	def fanStatus(self):
		return self._fanStatus

	@fanStatus.setter
	def fanStatus(self, value):
		self._fanStatus = value 

	@property
	def VFDFault(self):
		return self._VFDFault

	@VFDFault.setter
	def VFDFault(self, value):
		self._VFDFault = value  

	@property
	def HiStaticReset(self):
		return self._HiStaticReset

	@HiStaticReset.setter
	def HiStaticReset(self, value):
		self._HiStaticReset = value 

	@property
	def FAReturnFanShutdown(self):
		return self._FAReturnFanShutdown

	@FAReturnFanShutdown.setter
	def FAReturnFanShutdown(self, value):
		self._FAReturnFanShutdown = value   
		
	@property
	def fanVFD(self):
		return self._fanVFD

	@fanVFD.setter
	def fanVFD(self, value):
		self._fanVFD = value    
		
	@property
	def isolationDampers(self):
		return self._isolationDampers

	@isolationDampers.setter
	def isolationDampers(self, value):
		self._isolationDampers = value  
		
	@property
	def fanSS(self):
		return self._fanSS

	@fanSS.setter
	def fanSS(self, value):
		self._fanSS = value

	@property
	def airVelocityCFM(self):
		return self._airVelocityCFM

	@airVelocityCFM.setter
	def airVelocityCFM(self, value):
		self._airVelocityCFM = value

	@property
	def fan(self):
		return self._fan

	@fan.setter
	def fan(self, value):
		self._fan = value     

	def __str__(self):
		return "<FanReading(fanId = '%s', time_stamp = '%s', 'airVelocityPressure' = '%s' VFDSpeed = '%s', fanStatus = '%s', VFDFault = '%s',\
		 HiStaticReset = '%s', FAReturnFanShutdown = '%s',fanVFD = '%s',isolationDampers = '%s', fanSS = '%s', airVelocityCFM = '%s', fan = '%s')>" \
		% (self._fanId, self._time_stamp, self.airVelocityPressure, self._VFDSpeed, self._fanStatus, self._VFDFault, self._HiStaticReset,\
		 self._FAReturnFanShutdown, self._fanVFD, self._isolationDampers, self._fanSS, self._airVelocityCFM, str(self._fan))


class HEC(Base):
	"""Class to map to the HEC table in the HVAC DB"""

	__tablename__ = "Heat_Exchanger_Coil"

	_HECId = Column('HECId', Integer, primary_key = True, autoincrement = True)
	_AHUNumber = Column('AHUNumber', Integer, ForeignKey("Air_Handling_Unit.AHUNumber"), nullable = True)
	_SAVId = Column('SAVId', Integer, ForeignKey("Staged_Air_Volume.SAVId"), nullable = True)
	_VAVId = Column('VAVId', Integer, ForeignKey("Variable_Air_Volume.VAVId"), nullable = True)
	_HECName = Column('HECName', String(255))
	_HECType = Column('HECType', String(255))
	
	#Relationships
	
	_ahu = relationship("AHU", back_populates = "_hecs") #Relationship between HEC and AHU
	_vav = relationship("VAV", back_populates = "_hecs") #Relationship between HEC and VAV
	_sav = relationship("SAV", back_populates = "_hecs") #Relationship between HEC and SAV
	_hecReadings = relationship("HECReading", back_populates = "_hec") #Relationship between HEC and HEC_Reading

	#Constructor

	def __init__(self, HECId, HECName, HECType = None, AHUNumber = None, VAVId = None, SAVId = None, ahu = None, vav = None, sav = None, hecReadings = []):

		self._HECId = HECId
		self._HECName = HECName
		self._HECType = HECType
		self._AHUNumber = AHUNumber
		self._VAVId = VAVId
		self._SAVId = SAVId
		self._ahu = ahu
		self._vav = vav
		self._sav = sav
		self._hecReadings = hecReadings

	#Properties

	@property
	def HECId(self):
		return self._HECId

	@HECId.setter
	def HECId(self, value):
		self._HECId = value

	@property
	def HECName(self):
		return self._HECName

	@HECName.setter
	def HECName(self, value):
		self._HECName = value

	@property
	def HECType(self):
		return self._HECType

	@HECType.setter
	def HECType(self, value):
		self._HECType = value

	@property
	def AHUNumber(self):
		return self._AHUNumber

	@AHUNumber.setter
	def AHUNumber(self, value):
		self._AHUNumber = value

	@property
	def VAVId(self):
		return self._VAVId

	@VAVId.setter
	def VAVId(self, value):
		self._VAVId = value

	@property
	def SAVId(self):
		return self._SAVId

	@SAVId.setter
	def SAVId(self, value):
		self._SAVId = value

	@property
	def vav(self):
		return self._vav

	@vav.setter
	def vav(self, value):
		self._vav = value

	@property
	def sav(self):
		return self._sav

	@sav.setter
	def sav(self, value):
		self._sav = value

	@property
	def ahu(self):
		return self._ahu

	@ahu.setter
	def ahu(self, value):
		self._ahu = value

	@property
	def hecReadings(self):
		return self._hecReadings

	@hecReadings.setter
	def hecReadings(self, value):
		self._hecReadings = value

	#Methods

	def getComponentName(self):
		return self._HECName

	def getComponentType(self):
		return "HEC" + self._HECType

	def __str__(self):
		return "<HEC(HECId = '%d', AHUNumber = '%d', HECName = '%d', HECType = '%s', SAVId = '%d', VAVId = '%d', ahu = '%s', sav = '%s', vav = '%s', hecReadings = '%s')>" \
		% (self._HECId, self._AHUNumber, self._HECName, self._HECType, self._SAVId, self._VAVId, str(self._ahu), str(self._sav), str(self._vav), str(self._hecReadings))


class HECReading(Base):
	"""Class to map to the Heat Exchanger Coil Readings table in the HVAC DB"""

	__tablename__ = 'Heat_Exchanger_Coil_Reading'

	_HECId = Column('HECId', Integer, ForeignKey("Heat_Exchanger_Coil.HECId"), primary_key = True)
	_time_stamp = Column('Time_stamp', DateTime, primary_key = True)
	_supplyWaterTemperature = Column('SupplyWaterTemperature', Float, nullable=True)
	_returnWaterTemperature = Column('ReturnWaterTemperature', Float, nullable=True)
	_valveOpeningPercentage = Column('valveOpeningPercentage', Float, nullable=True)

	#Relationship between HEC Reading and HEC
	_hec = relationship("HEC", back_populates = "_hecReadings")
  
	#Constructor

	def __init__(self, HECId, time_stamp, supplyWaterTemperature, returnWaterTemperature = None, valveOpeningPercentage = None, hec = []):

		self._HECId = HECId
		self._time_stamp = time_stamp
		self._supplyWaterTemperature = supplyWaterTemperature
		self._returnWaterTemperature = returnWaterTemperature
		self._valveOpeningPercentage = valveOpeningPercentage
		self._hec = hec

	#properties

	@property
	def HECId(self):
		return self._HECId

	@HECId.setter
	def HECId(self, value):
		self._HECId = value

	@property
	def time_stamp(self):
		return self._time_stamp

	@time_stamp.setter
	def time_stamp(self, value):
		self._time_stamp = value

	@property
	def supplyWaterTemperature(self):
		return self._supplyWaterTemperature

	@supplyWaterTemperature.setter
	def supplyWaterTemperature(self, value):
		self._supplyWaterTemperature = value

	@property
	def returnWaterTemperature(self):
		return self._returnWaterTemperature

	@returnWaterTemperature.setter
	def returnWaterTemperature(self, value):
		self._returnWaterTemperature = value  

	@property
	def valveOpeningPercentage(self):
		return self._valveOpeningPercentage

	@valveOpeningPercentage.setter
	def valveOpeningPercentage(self, value):
		self._valveOpeningPercentage = value

	@property
	def hec(self):
		return self._hec

	@hec.setter
	def hec(self, value):
		self._hec = value   
		
	def __str__(self):
		return "<HECReading(HECId = '%s', time_stamp = '%s', supplyWaterTemperature = '%s', returnWaterTemperature = '%s', valveOpeningPercentage = '%s', hec = '%s')>" \
		% (self._HECId, self._time_stamp, self._supplyWaterTemperature, self._returnWaterTemperature, self._valveOpeningPercentage, str(self._hec))


class SAV(Base):
	"""Class to map to the SAV table in the HVAC DB"""

	__tablename__ = "Staged_Air_Volume"

	_SAVId = Column('SAVId', Integer, primary_key = True, autoincrement = True)
	_AHUNumber = Column('AHUNumber', Integer, ForeignKey("Air_Handling_Unit.AHUNumber"))
	_SAVName = Column('SAVName', String(255))
	
	#Relationships
	_ahu = relationship("AHU", back_populates = "_savs") #Relationship between SAV and AHU
	_hecs = relationship("HEC", back_populates = "_sav") #Relationship between SAV and HEC
	_thermafusers = relationship("Thermafuser", back_populates = "_sav") #Relationship between SAV and Thermafuser
	_savReadings = relationship("SAVReading", back_populates = "_sav") #Relationship between SAV and SAV_Reading

	#Constructor

	def __init__(self, SAVId, AHUNumber, SAVName, ahu = None, hecs = [], thermafusers = [], SAVReadings = []):

		self._SAVId = SAVId
		self._AHUNumber = AHUNumber
		self._SAVName = SAVName
		self._ahu = ahu
		self._hecs = hecs
		self._SAVReadings = SAVReadings
		self._thermafusers = thermafusers

	#Properties

	@property
	def SAVId(self):
		return self._SAVId

	@SAVId.setter
	def SAVId(self, value):
		self._SAVId = value

	@property
	def SAVName(self):
		return self._SAVName

	@SAVName.setter
	def SAVName(self, value):
		self._SAVName = value

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
	def hecs(self):
		return self._hecs

	@hecs.setter
	def hecs(self, value):
		self._hecs = value

	@property
	def thermafusers(self):
		return self._thermafusers

	@thermafusers.setter
	def thermafusers(self, value):
		self._thermafusers = value

	@property
	def SAVReadings(self):
		return self._SAVReadings

	@SAVReadings.setter
	def SAVReadings(self, value):
		self._SAVReadings = value

	#Methods

	def getComponentName(self):
		return self._SAVName

	def getComponentType(self):
		return "SAV"

	def __str__(self):
		return "<SAV(SAVId = '%d', AHUNumber = '%d', SAVName = '%d', ahu = '%s', hecs = '%s', thermafusers = '%s', SAVReadings = '%s')>" \
		% (self._SAVId, self._AHUNumber, self._SAVName, str(self._ahu), str(self._hecs), str(self._thermafusers), str(self._SAVReadings))


class SAVReading(Base):
	"""Class to map to the SAV Readings table in the HVAC DB"""

	__tablename__ = 'Staged_Air_Volume_Reading'

	_SAVId = Column('SAVId', Integer, ForeignKey("Staged_Air_Volume.SAVId"), primary_key = True)
	_time_stamp = Column('Time_stamp', DateTime, primary_key = True)
	_miscSpareInput = Column('MiscSpareInput', Float, nullable=True)
	_zoneTemperature = Column('ZoneTemperature', Float, nullable=True)
	_dischargeTemperature = Column('DischargeTemperature', Float, nullable=True)
	_miscInput = Column('MiscInput', Boolean, nullable=True)
	_condensateDetector = Column('CondensateDetector', Boolean, nullable=True)
	_valveOutputPercentage = Column('ValveOutputPercentage', Float, nullable=True)

	#Relationship between SAV Reading and SAV
	_sav = relationship("SAV", back_populates = "_savReadings")
  
	#Constructor

	def __init__(self, SAVId, time_stamp, miscSpareInput = None, zoneTemperature = None, dischargeTemperature = None, miscInput = None,\
	 condensateDetector = None, valveOutputPercentage = None, sav = None):

		self._SAVId = SAVId
		self._time_stamp = time_stamp
		self._miscSpareInput = miscSpareInput
		self._zoneTemperature = zoneTemperature
		self._dischargeTemperature = dischargeTemperature
		self._miscInput = miscInput
		self._condensateDetector = condensateDetector                
		self._valveOutputPercentage = valveOutputPercentage
		self._sav = sav

	#properties

	@property
	def SAVId(self):
		return self._SAVId

	@SAVId.setter
	def SAVId(self, value):
		self._SAVId = value

	@property
	def time_stamp(self):
		return self._time_stamp

	@time_stamp.setter
	def time_stamp(self, value):
		self._time_stamp = value

	@property
	def miscSpareInput(self):
		return self._miscSpareInput

	@miscSpareInput.setter
	def miscSpareInput(self, value):
		self._miscSpareInput = value

	@property
	def zoneTemperature(self):
		return self._zoneTemperature

	@zoneTemperature.setter
	def zoneTemperature(self, value):
		self._zoneTemperature = value   

	@property
	def dischargeTemperature(self):
		return self._dischargeTemperature

	@dischargeTemperature.setter
	def dischargeTemperature(self, value):
		self._dischargeTemperature = value  

	@property
	def miscInput(self):
		return self._miscInput

	@miscInput.setter
	def miscInput(self, value):
		self._miscInput = value 
	@property
	def condensateDetector(self):
		return self._condensateDetector

	@condensateDetector.setter
	def condensateDetector(self, value):
		self._condensateDetector = value    
		
	@property
	def valveOutputPercentage(self):
		return self._valveOutputPercentage

	@valveOutputPercentage.setter
	def valveOutputPercentage(self, value):
		self._valveOutputPercentage = value

	@property
	def sav(self):
		return self._sav

	@sav.setter
	def sav(self, value):
		self._sav = value   

	def __str__(self):
		return "<SAVReading(SAVId = '%s', time_stamp = '%s', miscSpareInput = '%s', zoneTemperature = '%s', dischargeTemperature = '%s',\
		 miscInput = '%s', condensateDetector = '%s', sav = '%s')>" \
		% (self._SAVId, self._time_stamp, self._miscSpareInput, self._zoneTemperature, self._dischargeTemperature, self._miscInput,\
		 self._condensateDetector,self._valveOutputPercentage, self._sav)


class VAV(Base):
	"""Class to map to the Filter table in the HVAC DB"""

	__tablename__ = "Variable_Air_Volume"

	_VAVId = Column('VAVId', Integer, primary_key = True, autoincrement = True)
	_AHUNumber = Column('AHUNumber', Integer, ForeignKey("Air_Handling_Unit.AHUNumber"))
	_VAVName = Column('VAVName', String(255))
	
	#Relationships
	_ahu = relationship("AHU", back_populates = "_vavs") #Relationship between VAV and AHU
	_hecs = relationship("HEC", back_populates = "_vav") #Relationship between VAV and HEC
	_thermafusers = relationship("Thermafuser", back_populates = "_vav") #Relationship between VAV and Thermafuser
	_vavReadings = relationship("VAVReading", back_populates = "_vav") #Relationship between VAV and VAV_Reading

	#Constructor

	def __init__(self, VAVId, AHUNumber, VAVName, ahu = None, hecs = [], thermafusers = [], VAVReadings = []):

		self._VAVId = VAVId
		self._AHUNumber = AHUNumber
		self._VAVName = VAVName
		self._ahu = ahu
		self._hecs = hecs
		self._VAVReadings = VAVReadings
		self._thermafusers = thermafusers

	#Properties

	@property
	def VAVId(self):
		return self._VAVId

	@VAVId.setter
	def VAVId(self, value):
		self._VAVId = value

	@property
	def VAVName(self):
		return self._VAVName

	@VAVName.setter
	def VAVName(self, value):
		self._VAVName = value

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
	def hecs(self):
		return self._hecs

	@hecs.setter
	def hecs(self, value):
		self._hecs = value

	@property
	def thermafusers(self):
		return self._thermafusers

	@thermafusers.setter
	def thermafusers(self, value):
		self._thermafusers = value

	@property
	def VAVReadings(self):
		return self._VAVReadings

	@VAVReadings.setter
	def VAVReadings(self, value):
		self._VAVReadings = value

	#Methods

	def getComponentName(self):
		return self._VAVName

	def getComponentType(self):
		return "VAV"

	def __str__(self):
		return "<VAV(VAVId = '%d', AHUNumber = '%d', VAVName = '%d', ahu = '%s', hecs = '%s', thermafusers = '%s', VAVReadings = '%s')>" \
		% (self._VAVId, self._AHUNumber, self._VAVName, str(self._ahu), str(self._hecs), str(self._thermafusers), str(self._VAVReadings))


class VAVReading(Base):
	"""Class to map to the VAV Readings table in the HVAC DB"""

	__tablename__ = 'Variable_Air_Volume_Reading'

	_VAVId = Column('VAVId', String(255), ForeignKey("Variable_Air_Volume.VAVId"), primary_key = True)
	_time_stamp = Column('Time_stamp', String(255), primary_key = True)
	_flowInput = Column('FlowInput', Float)
	_miscSpareInput = Column('MiscSpareInput', Float, nullable=True)
	_zoneTemperature = Column('ZoneTemperature', Float, nullable=True)
	_dischargeTemperature = Column('DischargeTemperature', Float, nullable=True)
	_condensateDetector = Column('CondensateDetector', Boolean, nullable=True)
	_ductStaticPressure = Column('DuctStaticPressure', String(255), nullable=True)
	_zoneCO2 = Column('ZoneCO2', Float, nullable=True)
	_damperPosition = Column('DamperPosition', Float, nullable=True)
	_coolingSetpoint = Column('CoolingSetpoint', Float, nullable=True)
	_heatingSetpoint = Column('HeatingSetpoint', Float, nullable=True)

	#Relationship between SAV Reading and SAV
	_vav = relationship("VAV", back_populates = "_vavReadings")
 
	#Constructor

	def __init__(self, VAVId, time_stamp, flowInput = None, miscSpareInput = None, zoneTemperature = None, dischargeTemperature = None,\
	 condensateDetector = None, ductStaticPressure = None, zoneCO2 = None, damperPosition = None, coolingSetpoint = None, heatingSetpoint = None, vav = None):

		self._VAVId = VAVId
		self._time_stamp = time_stamp
		self._flowInput = flowInput
		self._miscSpareInput = miscSpareInput
		self._zoneTemperature = zoneTemperature
		self._dischargeTemperature = dischargeTemperature
		self._condensateDetector = condensateDetector          
		self._ductStaticPressure = ductStaticPressure
		self._zoneCO2 = zoneCO2
		self._damperPosition = damperPosition
		self._coolingSetpoint = coolingSetpoint
		self._heatingSetpoint = heatingSetpoint
		self._vav = vav
		
	#properties

	@property
	def VAVId(self):
		return self._VAVId

	@VAVId.setter
	def VAVId(self, value):
		self._VAVId = value

	@property
	def time_stamp(self):
		return self._time_stamp

	@time_stamp.setter
	def time_stamp(self, value):
		self._time_stamp = value

	@property
	def flowInput(self):
		return self._flowInput

	@flowInput.setter
	def flowInput(self, value):
		self._flowInput = value

	@property
	def miscSpareInput(self):
		return self._miscSpareInput

	@miscSpareInput.setter
	def miscSpareInput(self, value):
		self._miscSpareInput = value    

	@property
	def zoneTemperature(self):
		return self._zoneTemperature

	@zoneTemperature.setter
	def zoneTemperature(self, value):
		self._zoneTemperature = value   

	@property
	def dischargeTemperature(self):
		return self._dischargeTemperature

	@dischargeTemperature.setter
	def dischargeTemperature(self, value):
		self._dischargeTemperature = value  
	@property
	def condensateDetector(self):
		return self._condensateDetector

	@condensateDetector.setter
	def condensateDetector(self, value):
		self._condensateDetector = value    
		
	@property
	def ductStaticPressure(self):
		return self._ductStaticPressure

	@ductStaticPressure.setter
	def ductStaticPressure(self, value):
		self._ductStaticPressure = value    
		
	@property
	def zoneCO2(self):
		return self._zoneCO2

	@zoneCO2.setter
	def zoneCO2(self, value):
		self._zoneCO2 = value   
		
	@property
	def damperPosition(self):
		return self._damperPosition

	@damperPosition.setter
	def damperPosition(self, value):
		self._damperPosition = value

	@property
	def coolingSetpoint(self):
		return self._coolingSetpoint

	@coolingSetpoint.setter
	def coolingSetpoint(self, value):
		self._coolingSetpoint = value

	@property
	def heatingSetpoint(self):
		return self._heatingSetpoint

	@heatingSetpoint.setter
	def heatingSetpoint(self, value):
		self._heatingSetpoint = value

	@property
	def vav(self):
		return self._vav

	@vav.setter
	def vav(self, value):
		self._vav = value

	def __str__(self):
		return "<VAVReading(VAVId = '%s', time_stamp = '%s', flowInput = '%s', miscSpareInput = '%s', zoneTemperature = '%s', dischargeTemperature = '%s',\
		 condensateDetector = '%s',ductStaticPressure = '%s',zoneCO2 = '%s', damperPosition = '%s', coolingSetpoint = '%s', heatingSetpoint = '%s', vav = '%s')>" \
		% (self._VAVId, self._time_stamp, self._flowInput, self._miscSpareInput, self._zoneTemperature, self._dischargeTemperature,\
		 self._condensateDetector, self._ductStaticPressure, self._zoneCO2, self._damperPosition, self._coolingSetpoint, self._heatingSetpoint, str(self._vav))


class Thermafuser(Base):
	"""Class to map to the Thermafuser table in the HVAC DB"""

	__tablename__ = "Thermafuser"

	_thermafuserId = Column('ThermafuserId', Integer, primary_key = True, autoincrement = True)
	_AHUNumber = Column('AHUNumber', Integer, ForeignKey("Air_Handling_Unit.AHUNumber"), nullable = True)
	_SAVId = Column('SAVId', Integer, ForeignKey("Staged_Air_Volume.SAVId"), nullable = True)
	_VAVId = Column('VAVId', Integer, ForeignKey("Variable_Air_Volume.VAVId"), nullable = True)
	_thermafuserName = Column('ThermafuserName', Integer)
	
	#Relationships
	
	_ahu = relationship("AHU", back_populates = "_thermafusers") #Relationship between Thermafuser and AHU
	_vav = relationship("VAV", back_populates = "_thermafusers") #Relationship between Thermafuser and VAV
	_sav = relationship("SAV", back_populates = "_thermafusers") #Relationship between Thermafuser and SAV
	_thermafuserReadings = relationship("ThermafuserReading", back_populates = "_thermafuser") #Relationship between HEC and HEC_Reading

	#Constructor

	def __init__(self, thermafuserId, thermafuserName, AHUNumber = None, VAVId = None, SAVId = None, ahu = None, vav = None, sav = None, thermafuserReadings = []):
		self._thermafuserName = thermafuserName
		self._AHUNumber = AHUNumber
		self._VAVId = VAVId
		self._SAVId = SAVId
		self._thermafuserId = thermafuserId
		self._ahu = ahu
		self._vav = vav
		self._sav = sav
		self._thermafuserReadings = thermafuserReadings

	#Properties

	@property
	def thermafuserId(self):
		return self._thermafuserId

	@thermafuserId.setter
	def thermafuserId(self, value):
		self._thermafuserId = value

	@property
	def thermafuserName(self):
		return self._thermafuserName

	@thermafuserName.setter
	def thermafuserName(self, value):
		self._thermafuserName = value

	@property
	def AHUNumber(self):
		return self._AHUNumber

	@AHUNumber.setter
	def AHUNumber(self, value):
		self._AHUNumber = value

	@property
	def VAVId(self):
		return self._VAVId

	@VAVId.setter
	def VAVId(self, value):
		self._VAVId = value

	@property
	def SAVId(self):
		return self._SAVId

	@SAVId.setter
	def SAVId(self, value):
		self._SAVId = value

	@property
	def ahu(self):
		return self._ahu

	@ahu.setter
	def ahu(self, value):
		self._ahu = value

	@property
	def vav(self):
		return self._vav

	@vav.setter
	def vav(self, value):
		self._vav = value

	@property
	def sav(self):
		return self._sav

	@sav.setter
	def sav(self, value):
		self._sav = value

	@property
	def thermafuserReadings(self):
		return self._thermafuserReadings

	@thermafuserReadings.setter
	def thermafuserReadings(self, value):
		self._thermafuserReadings = value

	#Methods

	def getComponentName(self):
		return self._thermafuserName

	def getComponentType(self):
		return "Thermafuser"

	def __str__(self):
		return "<Thermafuser(thermafuserId = '%d', AHUNumber = '%d', SAVId = '%d', VAVId = '%d', thermafuserName = '%d', ahu = '%s', sav = '%s', vav = '%s', thermafuserReadings = '%s')>" \
		% (self._thermafuserId, self._AHUNumber, self._SAVId, self._VAVId, self._thermafuserName, str(self._ahu), str(self._sav), str(self._vav), str(self._thermafuserReadings))


class ThermafuserReading(Base):
	"""Class to map to the Thermafuser Readings table in the HVAC DB"""

	__tablename__ = 'Thermafuser_Reading'

	_thermafuserId = Column('ThermafuserId', Integer, ForeignKey("Thermafuser.ThermafuserId"), primary_key = True)
	_time_stamp = Column('Time_stamp', DateTime, primary_key = True)
	_roomOccupied = Column('RoomOccupied', Boolean)
	_zoneTemperature = Column('ZoneTemperature', Float)
	_supplyAir = Column('SupplyAir', Float, nullable=True)
	_airflowFeedback = Column('AirflowFeedback', Float, nullable=True)
	_CO2Input = Column('CO2Input', Float, nullable=True)
	_maxAirflow = Column('MaxAirflow', Float, nullable=True)
	_minAirflow = Column('MinAirflow', Float, nullable=True)
	_unoccupiedHeatingSetpoint = Column('UnoccupiedHeatingSetpoint', Float, nullable=True)
	_unoccupiedCoolingSetpoint = Column('UnoccupiedCoolingSetpoint', Float, nullable=True)
	_occupiedCoolingSetpoint = Column('OccupiedCoolingSetpoint', Float, nullable=True)
	_occupiedHeatingSetpoint = Column('OccupiedHeatingSetpoint', Float, nullable=True)

	#Relationship between Thermafuser Reading and Thermafuser
	_thermafuser = relationship("Thermafuser", back_populates = "_thermafuserReadings")

	#Constructor

	def __init__(self, thermafuserId, time_stamp, roomOccupied = None, zoneTemperature = None, supplyAir = None, airflowFeedback = None, CO2Input = None, maxAirflow = None,\
	 minAirflow = None, unoccupiedHeatingSetpoint = None, unoccupiedCoolingSetpoint = None, occupiedCoolingSetpoint = None, occupiedHeatingSetpoint = None, thermafuser = None):
		self._thermafuserId = thermafuserId
		self._time_stamp = time_stamp
		self._roomOccupied = roomOccupied
		self._zoneTemperature = zoneTemperature
		self._supplyAir = supplyAir
		self._airflowFeedback = airflowFeedback
		self._CO2Input = CO2Input
		self._maxAirflow = maxAirflow                
		self._minAirflow = minAirflow
		self._unoccupiedHeatingSetpoint = unoccupiedHeatingSetpoint
		self._unoccupiedCoolingSetpoint = unoccupiedCoolingSetpoint
		self._occupiedCoolingSetpoint = occupiedCoolingSetpoint
		self._occupiedHeatingSetpoint = occupiedHeatingSetpoint
		self._thermafuser = thermafuser

	#properties

	@property
	def thermafuserId(self):
		return self._thermafuserId

	@thermafuserId.setter
	def thermafuserId(self, value):
		self._thermafuserId = value

	@property
	def time_stamp(self):
		return self._time_stamp

	@time_stamp.setter
	def time_stamp(self, value):
		self._time_stamp = value

	@property
	def roomOccupied(self):
		return self._roomOccupied

	@roomOccupied.setter
	def roomOccupied(self, value):
		self._roomOccupied = value

	@property
	def zoneTemperature(self):
		return self._zoneTemperature

	@zoneTemperature.setter
	def zoneTemperature(self, value):
		self._zoneTemperature = value

	@property
	def supplyAir(self):
		return self._supplyAir

	@supplyAir.setter
	def supplyAir(self, value):
		self._supplyAir = value 

	@property
	def airflowFeedback(self):
		return self._airflowFeedback

	@airflowFeedback.setter
	def airflowFeedback(self, value):
		self._airflowFeedback = value   

	@property
	def CO2Input(self):
		return self._CO2Input

	@CO2Input.setter
	def CO2Input(self, value):
		self._CO2Input = value  
	@property
	def maxAirflow(self):
		return self._maxAirflow

	@maxAirflow.setter
	def maxAirflow(self, value):
		self._maxAirflow = value    
		
	@property
	def minAirflow(self):
		return self._minAirflow

	@minAirflow.setter
	def minAirflow(self, value):
		self._minAirflow = value    
		
	@property
	def unoccupiedHeatingSetpoint(self):
		return self._unoccupiedHeatingSetpoint

	@unoccupiedHeatingSetpoint.setter
	def unoccupiedHeatingSetpoint(self, value):
		self._unoccupiedHeatingSetpoint = value 
		
	@property
	def unoccupiedCoolingSetpoint(self):
		return self._unoccupiedCoolingSetpoint

	@unoccupiedCoolingSetpoint.setter
	def unoccupiedCoolingSetpoint(self, value):
		self._unoccupiedCoolingSetpoint = value
		
	@property
	def occupiedCoolingSetpoint(self):
		return self._occupiedCoolingSetpoint

	@occupiedCoolingSetpoint.setter
	def occupiedCoolingSetpoint(self, value):
		self._occupiedCoolingSetpoint = value   
	
	@property
	def occupiedHeatingSetpoint(self):
		return self._occupiedHeatingSetpoint

	@occupiedHeatingSetpoint.setter
	def occupiedHeatingSetpoint(self, value):
		self._occupiedHeatingSetpoint = value   

	@property
	def thermafuser(self):
		return self._thermafuser

	@thermafuser.setter
	def thermafuser(self, value):
		self._thermafuser = value

	def __str__(self):
		return "<ThermafuserReading(thermafuserId = '%s', time_stamp = '%s', roomOccupied = '%s', zoneTemperature = '%s', supplyAir = '%s', airflowFeedback = '%s',\
		 CO2Input = '%s', maxAirflow = '%s',minAirflow = '%s',unoccupiedHeatingSetpoint = '%s', unoccupiedCoolingSetpoint = '%s',occupiedCoolingSetpoint = '%s',\
		 occupiedHeatingSetpoint = '%s', thermafuser = '%s')>" \
		% (self._thermafuserId, self._time_stamp, self._roomOccupied, self._zoneTemperature, self._supplyAir, self._airflowFeedback, self._CO2Input,\
		 self._maxAirflow,self._minAirflow,self._unoccupiedHeatingSetpoint,self._unoccupiedCoolingSetpoint, self._occupiedCoolingSetpoint,\
		  self._occupiedHeatingSetpoint, str(self._thermafuser))











