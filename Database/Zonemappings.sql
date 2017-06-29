use HVAC;

#Thermafuser
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m076", "Thermafuser Sensor", "Terminal Load", #Does not exist on database)
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m073", "Thermafuser", "Airflow Feedback", "Thermafuser_Reading.AirflowFeedback");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m135", "Thermafuser", "Occupied Cooling Setpoint", "Thermafuser_Reading.OccupiedCoolingSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m134", "Thermafuser", "Occupied Heating Setpoint", "Thermafuser_Reading.OccupiedHeatingSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m078", "Thermafuser", "Room Occupied", "Thermafuser_Reading.RoomOccupied");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m190", "Thermafuser", "Supply Air", "Thermafuser_Reading.SupplyAir");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m186", "Thermafuser", "Zone Temperature", "Thermafuser_Reading.ZoneTemperature");

#Heat Exchanger Coil
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("cw_valve", "Heat Exchanger Coil", "Chilled Water Valve Opening", "Heat_Exchanger_Coil.ValveOpeningPercentage");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("chw_valve", "Heat Exchanger Coil", "Chilled Water Valve Opening", "Heat_Exchanger_Coil.ValveOpeningPercentage");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("cwcr", "Heat Exchanger Coil", "Chilled Water Return Temperature", "Heat_Exchanger_Coil.ReturnWaterTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("cwcs", "Heat Exchanger Coil", "Chilled Water Supply Temperature", "Heat_Exchanger_Coil.SupplyWaterTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("hw_valve", "Heat Exchanger Coil", "Hot Water Valve Opening", "Heat_Exchanger_Coil.ValveOpeningPercentage");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("hwcr", "Heat Exchanger Coil", "Hot Water Return Temperature", "Heat_Exchanger_Coil.ReturnWaterTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("hwcs", "Heat Exchanger Coil", "Hot Water Supply Temperature", "Heat_Exchanger_Coil.SupplyWaterTemperature");

#Damper
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ea_dmpr", "Damper", "Exhaust Air Damper Opening", "Damper.OpeningPercentage");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("oa_dmpr", "Damper", "Outside Air Damper Opening", "Damper.OpeningPercentage");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ra_dmpr", "Damper", "Return Air Damper Opening", "Damper.OpeningPercentage");

#Filter
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ffilter_dp", "Filter", "Final Filter Difference Pressure", "Filter.DifferencePressure");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("pfilter_dp", "Filter", "Pre Filter Difference Pressure", "Filter.DifferencePressure");

#Fan
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sf,rf#_vel_press", "Fan", "Return Fan Velocity Pressure", "Fan.AirVelocityPressure");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sf,rf#_cfm_tnd", "Fan", "Return Fan CFM", "Fan.AirVelocityCFM");

#AHU
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m045", "AHU", "Number of Zones Requiring Cooling", "Air_Handling_Unit_Reading.CoolingRequest");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ahu/cl_stpt_tn", "AHU", "Cooling Setpoint", "Air_Handling_Unit_Reading.CoolingSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m044", "AHU", "Number of Zones Requiring Heating", "Air_Handling_Unit_Reading.HeatingRequest");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ahu/ht_stpt_tn", "AHU", "Heating Setpoint", "Air_Handling_Unit_Reading.HeatingSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("econ_stpt_tn", "AHU", "Economizer Setpoint", "Air_Handling_Unit_Reading.EconomizerSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ma_temp", "AHU", "Mixed Air Temp", "Air_Handling_Unit_Reading.MixedAirTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("oa_temperature", "AHU", "Outside Air Temp", "Air_Handling_Unit_Reading.OutsideAirTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m041", "AHU", "Occupied Mode", "Air_Handling_Unit_Reading.OccupiedMode");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("osa_co2", "AHU", "Outside Air Co2", "Air_Handling_Unit_Reading.OutsideAirCO2");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("osacfm", "AHU", "Outside Air Cfm", "Air_Handling_Unit_Reading.OutsideAirCFM");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("co2_stpt_tn", "AHU", "Return Air Co2 Setpoint", "Air_Handling_Unit_Reading.ReturnAirCO2Setpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ra_co2", "AHU", "Return Air Co2", "Air_Handling_Unit_Reading.ReturnAirCO2");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ra_temp", "AHU", "Return Air Temperature", "Air_Handling_Unit_Reading.ReturnAirTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m798", "AHU", "Static Pressure Smoothed", "Air_Handling_Unit_Reading.StaticPressureSmoothed");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m403", "AHU", "Static SP", "Air_Handling_Unit_Reading.StaticSP");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sa_temp", "AHU", "Supple Air Temperature", "Air_Handling_Unit_Reading.SupplyAirTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ra_sp", "AHU" , "Return Air Static Pressure", "Air_Handling_Unit_Reading.StaticPressure")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sa_stpt_tn", "AHU", "Supply Air Set Point", #"Can't find in database")

#VFD
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("power_kw_1610_tn", "VFD", "Power KW", "VFD_Reading.PowerKW");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("speed_rpm_1617_tn", "VFD", "Speed RPM", "VFD_Reading.SpeedRPM");

#VAV
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("vav/cl_stpt_tn", "VAV", "Cooling Setpoint", "Variable_Air_Volume_Reading.CoolingSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("vav/ht_stpt_tn", "VAV", "Heating Setpoint", "Variable_Air_Volume_Reading.HeatingSetpoint");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("da_temp", "VAV", "Discharge Temperature", "Variable_Air_Volume_Reading.DischargeTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("dmpr_pos_tn", "VAV", "Damper Position", "Variable_Air_Volume_Reading.DamperPosition");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("st_press", "VAV", "Duct Static Pressure", "Variable_Air_Volume_Reading.DuctStaticPressure");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("flow_input", "VAV", "Flow Control/Flow Input", "Variable_Air_Volume_Reading.FlowInput");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m311", "VAV", "Zone Temperature", "Variable_Air_Volume_Reading.ZoneTemperature");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m211", "VAV", "Static Setpoint 1", "Variable_Air_Volume_Reading.DuctStaticPressure");
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("zone_co2", "VAV", "Zone CO2", "Variable_Air_Volume_Reading.ZoneCO2");

#VFD
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("speed_rpm_1617_tn", "VFD", "1617 Speed RPM", "VFD_Reading.SpeedRPM")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("power_kw_1610_tn", "VFD", "1610 Power Kw", "VFD_Reading.PowerKW")
