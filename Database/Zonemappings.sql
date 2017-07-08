use HVAC;

#Thermafuser
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m076", "Thermafuser", "Terminal Load", "Thermafuser_Reading.TerminalLoad");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m073", "Thermafuser", "Airflow Feedback", "Thermafuser_Reading.airflowFeedback");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m135", "Thermafuser", "Occupied Cooling Setpoint", "Thermafuser_Reading.occupiedCoolingSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m134", "Thermafuser", "Occupied Heating Setpoint", "Thermafuser_Reading.occupiedHeatingSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m078", "Thermafuser", "Room Occupied", "Thermafuser_Reading.roomOccupied");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m190", "Thermafuser", "Supply Air", "Thermafuser_Reading.supplyAir");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m186", "Thermafuser", "Zone Temperature", "Thermafuser_Reading.zoneTemperature");

#Heat Exchanger Coil
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("cw_valve", "HEC", "Chilled Water Valve Opening", "Heat_Exchanger_Coil.valveOpeningPercentage");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("chw_valve", "HEC", "Chilled Water Valve Opening", "Heat_Exchanger_Coil.valveOpeningPercentage");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("cwcr", "HEC", "Chilled Water Return Temperature", "Heat_Exchanger_Coil.returnWaterTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("cwcs", "HEC", "Chilled Water Supply Temperature", "Heat_Exchanger_Coil.supplyWaterTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("hw_valve", "HEC", "Hot Water Valve Opening", "Heat_Exchanger_Coil.valveOpeningPercentage");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("hwcr", "HEC", "Hot Water Return Temperature", "Heat_Exchanger_Coil.returnWaterTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("hwcs", "HEC", "Hot Water Supply Temperature", "Heat_Exchanger_Coil.supplyWaterTemperature");

#Damper
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ea_dmpr", "Damper", "Exhaust Air Damper Opening", "Damper.damperOpeningPercentage");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("oa_dmpr", "Damper", "Outside Air Damper Opening", "Damper.damperOpeningPercentage");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ra_dmpr", "Damper", "Return Air Damper Opening", "Damper.damperOpeningPercentage");

#Filter
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ffilter_dp", "Filter", "Final Filter Difference Pressure", "Filter.differencePressure");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("pfilter_dp", "Filter", "Pre Filter Difference Pressure", "Filter.differencePressure");

#Fan
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("rf_vel_press", "Fan", "Return Fan Velocity Pressure", "Fan.airVelocityPressure");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("rf_cfm_tnd", "Fan", "Return Fan CFM", "Fan.AirVelocityCFM");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sf_vel_press", "Fan", "Supply Fan Velocity Pressure", "Fan.airVelocityPressure");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sf_cfm_tnd", "Fan", "Supply Fan CFM", "Fan.AirVelocityCFM");

#AHU
#Zone 4
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m045", "AHU", "Number of Zones Requiring Cooling", "Air_Handling_Unit_Reading.coolingRequest");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ahu/cl_stpt_tn", "AHU", "Cooling Setpoint", "Air_Handling_Unit_Reading.coolingSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m044", "AHU", "Number of Zones Requiring Heating", "Air_Handling_Unit_Reading.heatingRequest");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ahu/ht_stpt_tn", "AHU", "Heating Setpoint", "Air_Handling_Unit_Reading.heatingSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("econ_stpt_tn", "AHU", "Economizer Setpoint", "Air_Handling_Unit_Reading.economizerSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ma_temp", "AHU", "Mixed Air Temp", "Air_Handling_Unit_Reading.mixedAirTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("oa_temperature", "AHU", "Outside Air Temp", "Air_Handling_Unit_Reading.outsideAirTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m041", "AHU", "Occupied Mode", "Air_Handling_Unit_Reading.occupiedMode");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("osa_co2", "AHU", "Outside Air Co2", "Air_Handling_Unit_Reading.outsideAirCO2");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("osacfm", "AHU", "Outside Air Cfm", "Air_Handling_Unit_Reading.outsideAirCFM");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("co2_stpt_tn", "AHU", "Return Air Co2 Setpoint", "Air_Handling_Unit_Reading.returnAirCO2Setpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ra_co2", "AHU", "Return Air Co2", "Air_Handling_Unit_Reading.returnAirCO2");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ra_temp", "AHU", "Return Air Temperature", "Air_Handling_Unit_Reading.returnAirTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m798", "AHU", "Static Pressure Smoothed", "Air_Handling_Unit_Reading.staticPressureSmoothed");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m403", "AHU", "Static SP", "Air_Handling_Unit_Reading.staticSP");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sa_temp", "AHU", "Supple Air Temperature", "Air_Handling_Unit_Reading.supplyAirTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ra_sp", "AHU" , "Return Air Static Pressure", "Air_Handling_Unit_Reading.staticPressure");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sa_stpt_tn", "AHU", "Supply Air Set Point", "Air_Handling_Unit_Reading.SupplyAirSetpoint");

#VFD
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("power_kw_1610_tn", "VFD", "Power KW", "VFD_Reading.powerKW");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("speed_rpm_1617_tn", "VFD", "Speed RPM", "VFD_Reading.speedRPM");

#VAV
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("vav/cl_stpt_tn", "VAV", "Cooling Setpoint", "Variable_Air_Volume_Reading.coolingSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("vav/ht_stpt_tn", "VAV", "Heating Setpoint", "Variable_Air_Volume_Reading.heatingSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("da_temp", "VAV", "Discharge Temperature", "Variable_Air_Volume_Reading.dischargeTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("dmpr_pos_tn", "VAV", "Damper Position", "Variable_Air_Volume_Reading.damperPosition");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("st_press", "VAV", "Duct Static Pressure", "Variable_Air_Volume_Reading.ductStaticPressure");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("flow_input", "VAV", "Flow Control/Flow Input", "Variable_Air_Volume_Reading.flowInput");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m311", "VAV", "Zone Temperature", "Variable_Air_Volume_Reading.zoneTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m211", "VAV", "Static Setpoint 1", "Variable_Air_Volume_Reading.ductStaticPressure");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("zone_co2", "VAV", "Zone CO2", "Variable_Air_Volume_Reading.zoneCO2");
