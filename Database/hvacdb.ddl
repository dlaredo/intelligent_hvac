CREATE TABLE Thermafuser_Reading (
  Time_stamp                int(10) NOT NULL, 
  ThermafuserId             int(10) NOT NULL, 
  RoomOccupied              bit(1), 
  ZoneTemperature           real, 
  SupplyAir                 real, 
  AirflowFeedback           real, 
  CO2Input                  real, 
  MaxAirflow                real, 
  MinAirflow                real, 
  UnoccupiedHeatingSetpoint real, 
  UnoccupiedCoolingSetpoint real, 
  OccupiedCoolingSetpoint   real, 
  OccupiedHeatingSetpoint   real, 
  TerminalLoad              real, 
  PRIMARY KEY (Time_stamp, 
  ThermafuserId)) ENGINE=InnoDB;
CREATE TABLE Staged_Air_Volume_Reading (
  Time_stamp            datetime NOT NULL, 
  SAVId                 int(10) NOT NULL, 
  SAVName               varchar(255), 
  MiscSpareInput        real, 
  ZoneTemperature       real, 
  DischargeTemperature  real, 
  MiscInput             bit(1), 
  CondensateDetector    bit(1), 
  ValveOutputPercentage real, 
  PRIMARY KEY (Time_stamp, 
  SAVId)) ENGINE=InnoDB;
CREATE TABLE Air_Handling_Unit_Reading (
  AHUNumber              int(10) NOT NULL, 
  Time_stamp             datetime NOT NULL, 
  ZoneTemperature        real, 
  StaticPressure         real, 
  ReturnAirTemperature   real, 
  SupplyAirTemperature   real, 
  ExhaustAirTemperature  real, 
  OutsideAirTemperature  real, 
  SmokeDetector          bit(1), 
  OutsideAirCO2          real, 
  ReturnAirCO2           real, 
  Spare                  real, 
  HiStatic               bit(1), 
  DuctStaticPressure     real, 
  MixedAirTemperature    real, 
  OutsideAirCFM          real, 
  CoolingRequest         real, 
  CoolingSetpoint        real, 
  HeatingRequest         real, 
  HeatingSetpoint        real, 
  EconomizerSetpoint     real, 
  OccupiedMode           bit(1), 
  ReturnAirCO2Setpoint   real, 
  StaticPressureSmoothed real, 
  StaticSP               real, 
  SupplyAirSetpoint      real, 
  PRIMARY KEY (AHUNumber, 
  Time_stamp)) ENGINE=InnoDB;
CREATE TABLE Variable_Air_Volume_Reading (
  Time_stamp           datetime NOT NULL, 
  VAVId                int(10) NOT NULL, 
  VAVName              varchar(255), 
  FlowInput            real, 
  MiscSpareInput       real, 
  ZoneTemperature      real, 
  DischargeTemperature real, 
  CondensateDetector   bit(1), 
  DuctStaticPressure   real, 
  ZoneCO2              real, 
  DamperPosition       real, 
  CoolingSetpoint      real, 
  HeatingSetpoint      int(10), 
  PRIMARY KEY (Time_stamp, 
  VAVId)) ENGINE=InnoDB;
CREATE TABLE Heat_Exchanger_Coil_Reading (
  Time_stamp             datetime NOT NULL, 
  HECId                  int(10) NOT NULL, 
  IsHeatingCoil          bit(1) NOT NULL, 
  SupplyWaterTemperature real, 
  ReturnWaterTemperature real, 
  ValveOpeningPercentage real, 
  PRIMARY KEY (Time_stamp, 
  HECId)) ENGINE=InnoDB;
CREATE TABLE Filter_Reading (
  Time_stamp         datetime NOT NULL, 
  FilterId           int(10) NOT NULL, 
  FilterType         varchar(255) NOT NULL, 
  DifferencePressure real, 
  PRIMARY KEY (Time_stamp, 
  FilterId)) ENGINE=InnoDB;
CREATE TABLE Damper_Reading (
  Time_stamp              datetime NOT NULL, 
  DamperId                int(10) NOT NULL, 
  DamperType              varchar(255) NOT NULL, 
  DamperInputVoltage      real, 
  DamperOpeningPercentage real, 
  IsolationDamper         bit(1), 
  PRIMARY KEY (Time_stamp, 
  DamperId)) ENGINE=InnoDB;
CREATE TABLE Fan_Reading (
  Time_stamp          datetime NOT NULL, 
  FanId               int(10) NOT NULL, 
  FanType             varchar(255) NOT NULL, 
  AirVelocityPressure real, 
  VFDSpeed            real, 
  FanStatus           bit(1), 
  VFDFault            bit(1), 
  HiStaticReset       bit(1), 
  FAReturnFanShutdown bit(1), 
  FanVFD              bit(1), 
  IsolationDampers    bit(1), 
  FanSS               bit(1), 
  AirVelocityCFM      real, 
  PRIMARY KEY (Time_stamp, 
  FanId)) ENGINE=InnoDB;
CREATE TABLE Air_Handling_Unit (
  AHUNumber int(10) NOT NULL AUTO_INCREMENT, 
  PRIMARY KEY (AHUNumber)) ENGINE=InnoDB;
CREATE TABLE Fan (
  FanId     int(10) NOT NULL AUTO_INCREMENT, 
  AHUNumber int(10) NOT NULL, 
  FanNumber int(10) NOT NULL, 
  PRIMARY KEY (FanId)) ENGINE=InnoDB;
CREATE TABLE Damper (
  DamperId     int(10) NOT NULL AUTO_INCREMENT, 
  AHUNumber    int(10) NOT NULL, 
  DamperNumber int(10) NOT NULL, 
  PRIMARY KEY (DamperId)) ENGINE=InnoDB;
CREATE TABLE Filter (
  FilterId     int(10) NOT NULL AUTO_INCREMENT, 
  AHUNumber    int(10) NOT NULL, 
  FilterNumber int(10) NOT NULL, 
  PRIMARY KEY (FilterId)) ENGINE=InnoDB;
CREATE TABLE Staged_Air_Volume (
  SAVId     int(10) NOT NULL AUTO_INCREMENT, 
  AHUNumber int(10) NOT NULL, 
  SAVNumber int(10) NOT NULL, 
  PRIMARY KEY (SAVId)) ENGINE=InnoDB;
CREATE TABLE Variable_Air_Volume (
  VAVId     int(10) NOT NULL AUTO_INCREMENT, 
  AHUNumber int(10) NOT NULL, 
  VAVNumber int(10) NOT NULL, 
  PRIMARY KEY (VAVId)) ENGINE=InnoDB;
CREATE TABLE Heat_Exchanger_Coil (
  HECId     int(10) NOT NULL AUTO_INCREMENT, 
  AHUNumber int(10), 
  SAVId     int(10), 
  VAVId     int(10), 
  HECNumber int(10) NOT NULL, 
  PRIMARY KEY (HECId)) ENGINE=InnoDB;
CREATE TABLE Thermafuser (
  ThermafuserId     int(10) NOT NULL AUTO_INCREMENT, 
  SAVId             int(10), 
  VAVId             int(10), 
  ThermafuserNumber int(10) NOT NULL, 
  PRIMARY KEY (ThermafuserId)) ENGINE=InnoDB;
CREATE TABLE DataPoints (
  Path           varchar(255) NOT NULL, 
  Server         varchar(255) NOT NULL, 
  Location       varchar(255) NOT NULL, 
  Branch         varchar(255) NOT NULL, 
  SubBranch      varchar(255) NOT NULL, 
  ControlProgram varchar(255) NOT NULL, 
  Point          varchar(255) NOT NULL, 
  Zone           int(10) NOT NULL, 
  PRIMARY KEY (Path)) ENGINE=InnoDB;
CREATE TABLE PathMappings (
  Id              int(10) NOT NULL AUTO_INCREMENT, 
  Path            varchar(255) NOT NULL, 
  ComponentType   varchar(255) NOT NULL, 
  Description     varchar(255) NOT NULL, 
  DatabaseMapping varchar(255) NOT NULL, 
  PRIMARY KEY (Id)) ENGINE=InnoDB;
CREATE TABLE VFD (
  VFDId     int(10) NOT NULL AUTO_INCREMENT, 
  AHUNumber int(10) NOT NULL, 
  VFDNumber int(10) NOT NULL, 
  PRIMARY KEY (VFDId)) ENGINE=InnoDB;
CREATE TABLE VFD_Reading (
  VFDId      int(10) NOT NULL, 
  Time_stamp datetime NOT NULL, 
  VFDType    varchar(255) NOT NULL, 
  PowerKW    real, 
  SpeedRPM   real, 
  PRIMARY KEY (VFDId, 
  Time_stamp)) ENGINE=InnoDB;
ALTER TABLE Air_Handling_Unit_Reading ADD INDEX FKAir_Handli855032 (AHUNumber), ADD CONSTRAINT FKAir_Handli855032 FOREIGN KEY (AHUNumber) REFERENCES Air_Handling_Unit (AHUNumber);
ALTER TABLE Fan ADD INDEX FKFan812080 (AHUNumber), ADD CONSTRAINT FKFan812080 FOREIGN KEY (AHUNumber) REFERENCES Air_Handling_Unit (AHUNumber);
ALTER TABLE Damper ADD INDEX FKDamper841472 (AHUNumber), ADD CONSTRAINT FKDamper841472 FOREIGN KEY (AHUNumber) REFERENCES Air_Handling_Unit (AHUNumber);
ALTER TABLE Filter ADD INDEX FKFilter462060 (AHUNumber), ADD CONSTRAINT FKFilter462060 FOREIGN KEY (AHUNumber) REFERENCES Air_Handling_Unit (AHUNumber);
ALTER TABLE Damper_Reading ADD INDEX FKDamper_Rea482334 (DamperId), ADD CONSTRAINT FKDamper_Rea482334 FOREIGN KEY (DamperId) REFERENCES Damper (DamperId);
ALTER TABLE Staged_Air_Volume ADD INDEX FKStaged_Air556433 (AHUNumber), ADD CONSTRAINT FKStaged_Air556433 FOREIGN KEY (AHUNumber) REFERENCES Air_Handling_Unit (AHUNumber);
ALTER TABLE Staged_Air_Volume_Reading ADD INDEX FKStaged_Air505830 (SAVId), ADD CONSTRAINT FKStaged_Air505830 FOREIGN KEY (SAVId) REFERENCES Staged_Air_Volume (SAVId);
ALTER TABLE Variable_Air_Volume ADD INDEX FKVariable_A540853 (AHUNumber), ADD CONSTRAINT FKVariable_A540853 FOREIGN KEY (AHUNumber) REFERENCES Air_Handling_Unit (AHUNumber);
ALTER TABLE Heat_Exchanger_Coil ADD INDEX FKHeat_Excha729184 (AHUNumber), ADD CONSTRAINT FKHeat_Excha729184 FOREIGN KEY (AHUNumber) REFERENCES Air_Handling_Unit (AHUNumber);
ALTER TABLE Thermafuser ADD INDEX FKThermafuse134643 (SAVId), ADD CONSTRAINT FKThermafuse134643 FOREIGN KEY (SAVId) REFERENCES Staged_Air_Volume (SAVId);
ALTER TABLE Filter_Reading ADD INDEX FKFilter_Rea406158 (FilterId), ADD CONSTRAINT FKFilter_Rea406158 FOREIGN KEY (FilterId) REFERENCES Filter (FilterId);
ALTER TABLE Fan_Reading ADD INDEX FKFan_Readin671831 (FanId), ADD CONSTRAINT FKFan_Readin671831 FOREIGN KEY (FanId) REFERENCES Fan (FanId);
ALTER TABLE Heat_Exchanger_Coil ADD INDEX FKHeat_Excha285178 (SAVId), ADD CONSTRAINT FKHeat_Excha285178 FOREIGN KEY (SAVId) REFERENCES Staged_Air_Volume (SAVId);
ALTER TABLE Heat_Exchanger_Coil ADD INDEX FKHeat_Excha841889 (VAVId), ADD CONSTRAINT FKHeat_Excha841889 FOREIGN KEY (VAVId) REFERENCES Variable_Air_Volume (VAVId);
ALTER TABLE Heat_Exchanger_Coil_Reading ADD INDEX FKHeat_Excha620730 (HECId), ADD CONSTRAINT FKHeat_Excha620730 FOREIGN KEY (HECId) REFERENCES Heat_Exchanger_Coil (HECId);
ALTER TABLE Variable_Air_Volume_Reading ADD INDEX FKVariable_A451871 (VAVId), ADD CONSTRAINT FKVariable_A451871 FOREIGN KEY (VAVId) REFERENCES Variable_Air_Volume (VAVId);
ALTER TABLE Thermafuser ADD INDEX FKThermafuse308645 (VAVId), ADD CONSTRAINT FKThermafuse308645 FOREIGN KEY (VAVId) REFERENCES Variable_Air_Volume (VAVId);
ALTER TABLE Thermafuser_Reading ADD INDEX FKThermafuse935491 (ThermafuserId), ADD CONSTRAINT FKThermafuse935491 FOREIGN KEY (ThermafuserId) REFERENCES Thermafuser (ThermafuserId);
ALTER TABLE VFD ADD INDEX FKVFD797583 (AHUNumber), ADD CONSTRAINT FKVFD797583 FOREIGN KEY (AHUNumber) REFERENCES Air_Handling_Unit (AHUNumber);
ALTER TABLE VFD_Reading ADD INDEX FKVFD_Readin673303 (VFDId), ADD CONSTRAINT FKVFD_Readin673303 FOREIGN KEY (VFDId) REFERENCES VFD (VFDId);
