use HVAC;

CREATE TABLE Thermafuser_Reading (
  Time_stamp                int(10) NOT NULL, 
  ThermafuserNumber         int(10) NOT NULL, 
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
  PRIMARY KEY (Time_stamp, 
  ThermafuserNumber)) ENGINE=InnoDB;
CREATE TABLE Staged_Air_Volume_Reading (
  Time_stamp            datetime NOT NULL, 
  SAVNumber             int(10) NOT NULL, 
  SAVName               varchar(255), 
  MiscSpareInput        real, 
  ZoneTemperature       real, 
  DischargeTemperature  real, 
  MiscInput             bit(1), 
  CondensateDetector    bit(1), 
  ValveOutputPercentage real, 
  PRIMARY KEY (Time_stamp, 
  SAVNumber)) ENGINE=InnoDB;
CREATE TABLE Air_Handling_Unit_Reading (
  AHUNumber             int(10) NOT NULL, 
  Time_stamp            datetime NOT NULL, 
  ZoneTemperature       real, 
  StaticPressure        real, 
  ReturnAirTemperature  real, 
  SupplyAirTemperature  real, 
  ExhaustAirTemperature real, 
  OutsideAirTemperature real, 
  SmokeDetector         bit(1), 
  OutsideAirCO2         real, 
  ReturnAirCO2          real, 
  Spare                 real, 
  HiStatic              bit(1), 
  DuctStaticPressure    real, 
  MixedAirTemperature   real, 
  OSACFM                real, 
  PRIMARY KEY (AHUNumber, 
  Time_stamp)) ENGINE=InnoDB;
CREATE TABLE Variable_Air_Volume_Reading (
  Time_stamp           datetime NOT NULL, 
  VAVNumber            int(10) NOT NULL, 
  VAVName              varchar(255), 
  FlowInput            real, 
  MiscSpareInput       real, 
  ZoneTemperature      real, 
  DischargeTemperature real, 
  CondensateDetector   bit(1), 
  DuctStaticPressure   real, 
  ZoneCO2              real, 
  DamperPosition       real, 
  PRIMARY KEY (Time_stamp, 
  VAVNumber)) ENGINE=InnoDB;
CREATE TABLE Heat_Exchanger_Coil_Reading (
  Time_stamp             datetime NOT NULL, 
  HECNumber              int(10) NOT NULL, 
  isHotWaterSupply       bit(1) NOT NULL, 
  CoilType               varchar(255) NOT NULL, 
  WaterTemperature       real, 
  ValveOpeningPercentage real, 
  PRIMARY KEY (Time_stamp, 
  HECNumber)) ENGINE=InnoDB;
CREATE TABLE Filter_Reading (
  Time_stamp         datetime NOT NULL, 
  FilterNumber       int(10) NOT NULL, 
  FilterType         varchar(255) NOT NULL, 
  DifferencePressure real, 
  PRIMARY KEY (Time_stamp, 
  FilterNumber)) ENGINE=InnoDB;
CREATE TABLE Damper_Reading (
  DamperNumber            int(10) NOT NULL, 
  Time_stamp              datetime NOT NULL, 
  DamperType              varchar(255) NOT NULL, 
  DamperInputVoltage      real, 
  DamperOpeningPercentage real, 
  IsolationDamper         bit(1), 
  PRIMARY KEY (DamperNumber, 
  Time_stamp)) ENGINE=InnoDB;
CREATE TABLE Fan_Reading (
  Time_stamp          datetime NOT NULL, 
  FanNumber           int(10) NOT NULL, 
  FanType             bit(1) NOT NULL, 
  AirVelocityPressure real, 
  VFDSpeed            real, 
  FanStatus           bit(1), 
  VFDFault            bit(1), 
  HiStaticReset       bit(1), 
  FAReturnFanShutdown bit(1), 
  FanVFD              bit(1), 
  IsolationDampers    bit(1), 
  FanSS               bit(1), 
  PRIMARY KEY (Time_stamp, 
  FanNumber)) ENGINE=InnoDB;
CREATE TABLE Air_Handling_Unit (
  AHUNumber int(10) NOT NULL AUTO_INCREMENT, 
  PRIMARY KEY (AHUNumber)) ENGINE=InnoDB;
CREATE TABLE Fan (
  AHUNumber int(10) NOT NULL, 
  FanNumber int(10) NOT NULL AUTO_INCREMENT, 
  PRIMARY KEY (FanNumber)) ENGINE=InnoDB;
CREATE TABLE Damper (
  DamperNumber int(10) NOT NULL AUTO_INCREMENT, 
  AHUNumber    int(10) NOT NULL, 
  PRIMARY KEY (DamperNumber)) ENGINE=InnoDB;
CREATE TABLE Filter (
  FilterNumber int(10) NOT NULL AUTO_INCREMENT, 
  AHUNumber    int(10) NOT NULL, 
  PRIMARY KEY (FilterNumber)) ENGINE=InnoDB;
CREATE TABLE Staged_Air_Volume (
  SAVNumber int(10) NOT NULL AUTO_INCREMENT, 
  AHUNumber int(10) NOT NULL, 
  PRIMARY KEY (SAVNumber)) ENGINE=InnoDB;
CREATE TABLE Variable_Air_Volume (
  VAVNumber int(10) NOT NULL AUTO_INCREMENT, 
  AHUNumber int(10) NOT NULL, 
  PRIMARY KEY (VAVNumber)) ENGINE=InnoDB;
CREATE TABLE Heat_Exchanger_Coil (
  HECNumber int(10) NOT NULL AUTO_INCREMENT, 
  AHUNumber int(10), 
  SAVNumber int(10), 
  VAVNumber int(10), 
  PRIMARY KEY (HECNumber)) ENGINE=InnoDB;
CREATE TABLE Thermafuser (
  ThermafuserNumber int(10) NOT NULL AUTO_INCREMENT, 
  SAVNumber         int(10), 
  VAVNumber         int(10), 
  PRIMARY KEY (ThermafuserNumber)) ENGINE=InnoDB;
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
ALTER TABLE Air_Handling_Unit_Reading ADD INDEX FKAir_Handli855032 (AHUNumber), ADD CONSTRAINT FKAir_Handli855032 FOREIGN KEY (AHUNumber) REFERENCES Air_Handling_Unit (AHUNumber);
ALTER TABLE Fan ADD INDEX FKFan812080 (AHUNumber), ADD CONSTRAINT FKFan812080 FOREIGN KEY (AHUNumber) REFERENCES Air_Handling_Unit (AHUNumber);
ALTER TABLE Damper ADD INDEX FKDamper841472 (AHUNumber), ADD CONSTRAINT FKDamper841472 FOREIGN KEY (AHUNumber) REFERENCES Air_Handling_Unit (AHUNumber);
ALTER TABLE Filter ADD INDEX FKFilter462060 (AHUNumber), ADD CONSTRAINT FKFilter462060 FOREIGN KEY (AHUNumber) REFERENCES Air_Handling_Unit (AHUNumber);
ALTER TABLE Damper_Reading ADD INDEX FKDamper_Rea97083 (DamperNumber), ADD CONSTRAINT FKDamper_Rea97083 FOREIGN KEY (DamperNumber) REFERENCES Damper (DamperNumber);
ALTER TABLE Staged_Air_Volume ADD INDEX FKStaged_Air556433 (AHUNumber), ADD CONSTRAINT FKStaged_Air556433 FOREIGN KEY (AHUNumber) REFERENCES Air_Handling_Unit (AHUNumber);
ALTER TABLE Staged_Air_Volume_Reading ADD INDEX FKStaged_Air713034 (SAVNumber), ADD CONSTRAINT FKStaged_Air713034 FOREIGN KEY (SAVNumber) REFERENCES Staged_Air_Volume (SAVNumber);
ALTER TABLE Variable_Air_Volume ADD INDEX FKVariable_A540853 (AHUNumber), ADD CONSTRAINT FKVariable_A540853 FOREIGN KEY (AHUNumber) REFERENCES Air_Handling_Unit (AHUNumber);
ALTER TABLE Heat_Exchanger_Coil ADD INDEX FKHeat_Excha729184 (AHUNumber), ADD CONSTRAINT FKHeat_Excha729184 FOREIGN KEY (AHUNumber) REFERENCES Air_Handling_Unit (AHUNumber);
ALTER TABLE Thermafuser ADD INDEX FKThermafuse84222 (SAVNumber), ADD CONSTRAINT FKThermafuse84222 FOREIGN KEY (SAVNumber) REFERENCES Staged_Air_Volume (SAVNumber);
ALTER TABLE Filter_Reading ADD INDEX FKFilter_Rea372187 (FilterNumber), ADD CONSTRAINT FKFilter_Rea372187 FOREIGN KEY (FilterNumber) REFERENCES Filter (FilterNumber);
ALTER TABLE Fan_Reading ADD INDEX FKFan_Readin97693 (FanNumber), ADD CONSTRAINT FKFan_Readin97693 FOREIGN KEY (FanNumber) REFERENCES Fan (FanNumber);
ALTER TABLE Heat_Exchanger_Coil ADD INDEX FKHeat_Excha933686 (SAVNumber), ADD CONSTRAINT FKHeat_Excha933686 FOREIGN KEY (SAVNumber) REFERENCES Staged_Air_Volume (SAVNumber);
ALTER TABLE Heat_Exchanger_Coil ADD INDEX FKHeat_Excha259043 (VAVNumber), ADD CONSTRAINT FKHeat_Excha259043 FOREIGN KEY (VAVNumber) REFERENCES Variable_Air_Volume (VAVNumber);
ALTER TABLE Heat_Exchanger_Coil_Reading ADD INDEX FKHeat_Excha992142 (HECNumber), ADD CONSTRAINT FKHeat_Excha992142 FOREIGN KEY (HECNumber) REFERENCES Heat_Exchanger_Coil (HECNumber);
ALTER TABLE Variable_Air_Volume_Reading ADD INDEX FKVariable_A34718 (VAVNumber), ADD CONSTRAINT FKVariable_A34718 FOREIGN KEY (VAVNumber) REFERENCES Variable_Air_Volume (VAVNumber);
ALTER TABLE Thermafuser ADD INDEX FKThermafuse891491 (VAVNumber), ADD CONSTRAINT FKThermafuse891491 FOREIGN KEY (VAVNumber) REFERENCES Variable_Air_Volume (VAVNumber);
ALTER TABLE Thermafuser_Reading ADD INDEX FKThermafuse137097 (ThermafuserNumber), ADD CONSTRAINT FKThermafuse137097 FOREIGN KEY (ThermafuserNumber) REFERENCES Thermafuser (ThermafuserNumber);
