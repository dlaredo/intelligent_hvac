use HVAC2017;

#Thermafuser
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m076", "Thermafuser", "Terminal Load", "terminalLoad");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m073", "Thermafuser", "Airflow Feedback", "airflowFeedback");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m135", "Thermafuser", "Occupied Cooling Setpoint", "occupiedCoolingSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m134", "Thermafuser", "Occupied Heating Setpoint", "occupiedHeatingSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m078", "Thermafuser", "Room Occupied", "roomOccupied");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m190", "Thermafuser", "Supply Air", "supplyAir");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m186", "Thermafuser", "Zone Temperature", "zoneTemperature");

#Heat Exchanger Coil
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("cw_valve", "HEC", "Chilled Water Valve Opening", "valveOpeningPercentage");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("chw_valve", "HEC", "Chilled Water Valve Opening", "valveOpeningPercentage");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("cwcr", "HEC", "Chilled Water Return Temperature", "returnWaterTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("cwcs", "HEC", "Chilled Water Supply Temperature", "supplyWaterTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("hw_valve", "HEC", "Hot Water Valve Opening", "valveOpeningPercentage");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("hwcr", "HEC", "Hot Water Return Temperature", "returnWaterTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("hwcs", "HEC", "Hot Water Supply Temperature", "supplyWaterTemperature");

#Damper_Reading
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ea_dmpr", "Damper", "Exhaust Air Damper Opening", "damperOpeningPercentage");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("oa_dmpr", "Damper", "Outside Air Damper Opening", "damperOpeningPercentage");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ra_dmpr", "Damper", "Return Air Damper Opening", "damperOpeningPercentage");

#Filter
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ffilter_dp", "Filter", "Final Filter Difference Pressure", "differencePressure");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("pfilter_dp", "Filter", "Pre Filter Difference Pressure", "differencePressure");

#Fan
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("rf_vel_press", "Fan", "Return Fan Velocity Pressure", "airVelocityPressure");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("rf_cfm_tnd", "Fan", "Return Fan CFM", "airVelocityCFM");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sf_vel_press", "Fan", "Supply Fan Velocity Pressure", "airVelocityPressure");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sf_cfm_tnd", "Fan", "Supply Fan CFM", "airVelocityCFM");

#AHU
#Zone 4
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ahu/m045", "AHU", "Number of Zones Requiring Cooling", "coolingRequest");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ahu/cl_stpt_tn", "AHU", "Cooling Setpoint", "coolingSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ahu/m044", "AHU", "Number of Zones Requiring Heating", "heatingRequest");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ahu/ht_stpt_tn", "AHU", "Heating Setpoint", "heatingSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("econ_stpt_tn", "AHU", "Economizer Setpoint", "economizerSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ma_temp", "AHU", "Mixed Air Temp", "mixedAirTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("oa_temperature", "AHU", "Outside Air Temp", "outsideAirTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m041", "AHU", "Occupied Mode", "occupiedMode");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("osa_co2", "AHU", "Outside Air Co2", "outsideAirCO2");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("osacfm", "AHU", "Outside Air Cfm", "outsideAirCFM");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("co2_stpt_tn", "AHU", "Return Air Co2 Setpoint", "returnAirCO2Setpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ra_co2", "AHU", "Return Air Co2", "returnAirCO2");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ra_temp", "AHU", "Return Air Temperature", "returnAirTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m798", "AHU", "Static Pressure Smoothed", "staticPressureSmoothed");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m403", "AHU", "Static SP", "staticSP");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sa_temp", "AHU", "Supple Air Temperature", "supplyAirTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ra_sp", "AHU" , "Return Air Static Pressure", "staticPressure");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sa_stpt_tn", "AHU", "Supply Air Set Point", "supplyAirSetpoint");
#Zone 3
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("st_press1","AHU","Static Pressure 2 A", "staticPressure");
#Zones 1_2
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m496","AHU","ST Req", "STReq");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m124","AHU","Static SP1", "staticSP1");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m415","AHU","Static SP2", "staticSP2");

#VFD
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("power_kw_1610_tn", "VFD", "Power KW", "powerKW");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("speed_rpm_1617_tn", "VFD", "Speed RPM", "speedRPM");

#VAV
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("vav/cl_stpt_tn", "VAV", "Cooling Setpoint", "coolingSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("vav/ht_stpt_tn", "VAV", "Heating Setpoint", "heatingSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("vav/da_temp", "VAV", "Discharge Temperature", "dischargeTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("dmpr_pos_tn", "VAV", "Damper_Reading Position", "damperPosition");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("st_press", "VAV", "Duct Static Pressure", "ductStaticPressure");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("flow_input", "VAV", "Flow Control/Flow Input", "flowInput");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m311", "VAV", "Zone Temperature", "zoneTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m211", "VAV", "Static Setpoint 1", "ductStaticPressure");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("zone_co2", "VAV", "Zone CO2", "zoneCO2");

#SAV 
#Zone 1 & 2 
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m277", "SAV", "GEX Damper Position","GEXDamperPosition");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m285", "SAV", "Heating requests", "coolingRequest");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m288", "SAV", "Cooling requests", "heatingRequest");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m310", "SAV", "SAV Damper Position", "damperPosition");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m318", "SAV", "Exhaust Air Flow", "exhaustAirflow");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m320", "SAV", "Supply Air Flow", "supplyAirflow");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m322", "SAV", "Flow Difference", "flowDifference");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m328", "SAV", "Exhaust Flow Setpoint", "exhaustFlowSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sav/da_temp", "SAV", "Discharge Temperature", "dischargeTemperature"); 
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("cl_pct_tn", "SAV", "Cooling Percentage","heatingPercentage");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ht_pct_tn", "SAV", "Heating Percentage","coolingPercentage");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sav/cl_stpt_tn", "SAV", "Cooling Setpoint", "coolingSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sav/ht_stpt_tn", "SAV", "Heating Setpoint", "heatingSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("zone_temp", "SAV", "Zone Temperature", "zoneTemperature"); 
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m423", "SAV", "CER Temperature","CERTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sav/m044", "SAV", "Number of Zones Requiring Heating", "htRequest");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sav/m045", "SAV", "Number of Zones Requiring Cooling", "clRequest");
