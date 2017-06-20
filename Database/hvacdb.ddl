CREATE TABLE Air_Handling_Unit (
  AHUNumber             int(10) NOT NULL, 
  Time_stamp            datetime NOT NULL, 
  ZoneTemperature       real NOT NULL, 
  StaticPressure        real NOT NULL, 
  ReturnAirTemperature  real, 
  SupplyAirTemperature  real, 
  ExhaustAirTemperature real, 
  OutsideAirTemperature real, 
  SmokeDetector         tinyint, 
  OutsideAirCO2         real, 
  ReturnAirCO2          real, 
  Spare                 real, 
  HiStatic              tinyint, 
  DuctStaticPressure    real, 
  MixedAirTemperature   real, 
  OSACFM                real, 
  PRIMARY KEY (AHUNumber, 
  Time_stamp)) ENGINE=InnoDB;
CREATE TABLE Fan (
  FanNumber           int(10) NOT NULL, 
  AHUNumber           int(10) NOT NULL, 
  AHUTime_stamp       datetime NOT NULL, 
  FanType             tinyint(1) NOT NULL, 
  AirVelocityPressure real, 
  VFDSpeed            real, 
  FanStatus           tinyint(1), 
  VFDFault            tinyint, 
  HiStaticReset       tinyint, 
  FAReturnFanShutdown tinyint, 
  FanVFD              tinyint, 
  IsolationDampers    tinyint, 
  FanSS               tinyint, 
  PRIMARY KEY (FanNumber, 
  AHUTime_stamp)) ENGINE=InnoDB;
CREATE TABLE Damper (
  DamperNumber            int(10) NOT NULL, 
  AHUNumber               int(10) NOT NULL, 
  AHUTime_stamp           datetime NOT NULL, 
  DamperType              varchar(255) NOT NULL, 
  DamperInputVoltage      real, 
  DamperOpeningPercentage real, 
  IsolationDamper         tinyint, 
  PRIMARY KEY (DamperNumber, 
  AHUTime_stamp)) ENGINE=InnoDB;
CREATE TABLE Filter (
  FilterNumber       int(10) NOT NULL, 
  AHUNumber          int(10) NOT NULL, 
  AHUTime_stamp      datetime NOT NULL, 
  FilterType         varchar(255) NOT NULL, 
  DifferencePressure real, 
  PRIMARY KEY (FilterNumber, 
  AHUTime_stamp)) ENGINE=InnoDB;
CREATE TABLE Heat_Exchanger_Coil (
  HECoilNumber           int(10) NOT NULL, 
  AHUNumber              int(10), 
  SAVNumber              int(10), 
  VAVNumber              int(10), 
  AHUTime_stamp          datetime NOT NULL, 
  SAVAHUTime_stamp       datetime NOT NULL, 
  VAVAHUTime_stamp       datetime NOT NULL, 
  isHotWaterSupply       tinyint NOT NULL, 
  CoilType               varchar(255) NOT NULL, 
  WaterTemperature       real, 
  ValveOpeningPercentage real, 
  PRIMARY KEY (HECoilNumber, 
  AHUTime_stamp, 
  SAVAHUTime_stamp, 
  VAVAHUTime_stamp)) ENGINE=InnoDB;
CREATE TABLE Staged_Air_Volume (
  SAVNumber             int(10) NOT NULL, 
  AHUNumber             int(10) NOT NULL, 
  AHUTime_stamp         datetime NOT NULL, 
  SAVName               varchar(255), 
  MiscSpareInput        real, 
  ZoneTemperature       real, 
  DischargeTemperature  real, 
  MiscInput             tinyint, 
  CondensateDetector    tinyint, 
  ValveOutputPercentage real, 
  PRIMARY KEY (SAVNumber, 
  AHUTime_stamp)) ENGINE=InnoDB;
CREATE TABLE Variable_Air_Volume (
  VAVNumber            int(10) NOT NULL, 
  AHUNumber            int(10) NOT NULL, 
  AHUTime_stamp        datetime NOT NULL, 
  VAVName              varchar(255), 
  FlowInput            real, 
  MiscSpareInput       real, 
  ZoneTemperature      real, 
  DischargeTemperature real, 
  CondensateDetector   tinyint, 
  DuctStaticPressure   real, 
  ZoneCO2              real, 
  DamperPosition       real, 
  PRIMARY KEY (VAVNumber, 
  AHUTime_stamp)) ENGINE=InnoDB;
CREATE TABLE Thermafuser (
  ThermafuserNumber         int(10) NOT NULL, 
  SAVNumber                 int(10), 
  VAVNumber                 int(10), 
  SAVAHUTime_stamp          datetime NOT NULL, 
  VAVAHUTime_stamp          datetime NOT NULL, 
  RoomOccupied              tinyint, 
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
  PRIMARY KEY (ThermafuserNumber, 
  SAVAHUTime_stamp, 
  VAVAHUTime_stamp)) ENGINE=InnoDB;
ALTER TABLE Fan ADD INDEX Has3 (AHUNumber, AHUTime_stamp), ADD CONSTRAINT Has3 FOREIGN KEY (AHUNumber, AHUTime_stamp) REFERENCES Air_Handling_Unit (AHUNumber, Time_stamp);
ALTER TABLE Damper ADD INDEX Has1 (AHUNumber, AHUTime_stamp), ADD CONSTRAINT Has1 FOREIGN KEY (AHUNumber, AHUTime_stamp) REFERENCES Air_Handling_Unit (AHUNumber, Time_stamp);
ALTER TABLE Filter ADD INDEX Has2 (AHUNumber, AHUTime_stamp), ADD CONSTRAINT Has2 FOREIGN KEY (AHUNumber, AHUTime_stamp) REFERENCES Air_Handling_Unit (AHUNumber, Time_stamp);
ALTER TABLE Staged_Air_Volume ADD INDEX Supplies (AHUNumber, AHUTime_stamp), ADD CONSTRAINT Supplies FOREIGN KEY (AHUNumber, AHUTime_stamp) REFERENCES Air_Handling_Unit (AHUNumber, Time_stamp);
ALTER TABLE Variable_Air_Volume ADD INDEX Supplies3 (AHUNumber, AHUTime_stamp), ADD CONSTRAINT Supplies3 FOREIGN KEY (AHUNumber, AHUTime_stamp) REFERENCES Air_Handling_Unit (AHUNumber, Time_stamp);
ALTER TABLE Thermafuser ADD INDEX Supplies2 (VAVNumber, VAVAHUTime_stamp), ADD CONSTRAINT Supplies2 FOREIGN KEY (VAVNumber, VAVAHUTime_stamp) REFERENCES Variable_Air_Volume (VAVNumber, AHUTime_stamp);
ALTER TABLE Thermafuser ADD INDEX Supplies1 (SAVNumber, SAVAHUTime_stamp), ADD CONSTRAINT Supplies1 FOREIGN KEY (SAVNumber, SAVAHUTime_stamp) REFERENCES Staged_Air_Volume (SAVNumber, AHUTime_stamp);
ALTER TABLE Heat_Exchanger_Coil ADD INDEX Has6 (VAVNumber, VAVAHUTime_stamp), ADD CONSTRAINT Has6 FOREIGN KEY (VAVNumber, VAVAHUTime_stamp) REFERENCES Variable_Air_Volume (VAVNumber, AHUTime_stamp);
ALTER TABLE Heat_Exchanger_Coil ADD INDEX Has4 (AHUNumber, AHUTime_stamp), ADD CONSTRAINT Has4 FOREIGN KEY (AHUNumber, AHUTime_stamp) REFERENCES Air_Handling_Unit (AHUNumber, Time_stamp);
ALTER TABLE Heat_Exchanger_Coil ADD INDEX Has5 (SAVNumber, SAVAHUTime_stamp), ADD CONSTRAINT Has5 FOREIGN KEY (SAVNumber, SAVAHUTime_stamp) REFERENCES Staged_Air_Volume (SAVNumber, AHUTime_stamp);
