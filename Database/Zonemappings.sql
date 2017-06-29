
#Thermafuser
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m073", "Thermafuser Sensor", "Airflow Feedback", "Thermafuser_Reading.AirflowFeedback")
<<<<<<< HEAD
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m135", "Thermafuser Sensor", "OccupiedCoolingSetpoint", "Thermafuser_Reading.OccupiedCoolingSetpoint")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m134", "Thermafuser Sensor", "OccupiedHeatingSetpoint", "Thermafuser_Reading.OccupiedHeatingSetpoint")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m078", "Thermafuser Sensor", "RoomOccupied", "Thermafuser_Reading.RoomOccupied")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m190", "Thermafuser Sensor", "SupplyAir", "Thermafuser_Reading.SupplyAir")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m186", "Thermafuser Sensor", "ZoneTemperature", "Thermafuser_Reading.ZoneTemperature")
#Zone 3
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m076", "Thermafuser Sensor", "Terminal Load", #Does not exist on database)
=======
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m135", "Thermafuser Sensor", "Occupied Cooling Setpoint", "Thermafuser_Reading.OccupiedCoolingSetpoint")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m134", "Thermafuser Sensor", "Occupied Heating Setpoint", "Thermafuser_Reading.OccupiedHeatingSetpoint")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m078", "Thermafuser Sensor", "Room Occupied", "Thermafuser_Reading.RoomOccupied")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m190", "Thermafuser Sensor", "Supply Air", "Thermafuser_Reading.SupplyAir")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m186", "Thermafuser Sensor", "Zone Temperature", "Thermafuser_Reading.ZoneTemperature")
>>>>>>> f85d9bc962bfaef9d619d51a232f7a91510e7ae4

#Heat Exchanger Coil
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("cw_valve", "Heat Exchanger Coil", "Chilled Water Valve Opening", "Heat_Exchanger_Coil.ValveOpeningPercentage")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("chw_valve", "Heat Exchanger Coil", "Chilled Water Valve Opening", "Heat_Exchanger_Coil.ValveOpeningPercentage")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("cwcr", "Heat Exchanger Coil", "Chilled Water Return Temperature", "Heat_Exchanger_Coil.ReturnWaterTemperature")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("cwcs", "Heat Exchanger Coil", "Chilled Water Supply Temperature", "Heat_Exchanger_Coil.SupplyWaterTemperature")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("hw_valve", "Heat Exchanger Coil", "Hot Water Valve Opening", "Heat_Exchanger_Coil.ValveOpeningPercentage")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("hwcr", "Heat Exchanger Coil", "Hot Water Return Temperature", "Heat_Exchanger_Coil.ReturnWaterTemperature")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("hwcs", "Heat Exchanger Coil", "Hot Water Supply Temperature", "Heat_Exchanger_Coil.SupplyWaterTemperature")

#Damper
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ea_dmpr", "Damper", "Exhaust Air Damper Opening", "Damper.OpeningPercentage")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("oa_dmpr", "Damper", "Outside Air Damper Opening", "Damper.OpeningPercentage")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ra_dmpr", "Damper", "Return Air Damper Opening", "Damper.OpeningPercentage")

#Filter
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ffilter_dp", "Filter", "Final Filter Difference Pressure", "Filter.DifferencePressure")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("pfilter_dp", "Filter", "Pre Filter Difference Pressure", "Filter.DifferencePressure")

#Fan
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sf\rf#_vel_press", "Fan", "Return Fan Velocity Pressure", "Fan_Reading.AirVelocityPressure")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sf\rf#_cfm_tnd", "Fan", "Return Fan CFM", "Fan_Reading.AirVelocityCFM")
#Zone 3
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sf4_cfm_tnd", "Fan", "Supply Fan 4 CFM", "Fan_Reading.AirVelocityCFM")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sf_cfm_tnd", "Fan", "Supply Fan 3 Total CFM", "Fan_Reading.AirVelocityCFM")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sf3_cfm_tnd", "Fan", "Supply Fan 3 CFM", "Fan_Reading.AirVelocityCFM")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sf2_cfm_tnd", "Fan", "Supply Fan 2 CFM", "Fan_Reading.AirVelocityCFM")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sf1_cfm_tnd", "Fan", "Supply Fan 1 CFM", "Fan_Reading.AirVelocityCFM")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sf4_vel_press", "Fan", "Supply Fan 3D Velocity Pressure", "Fan_Reading.AirVelocityPressure")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sf3_vel_press", "Fan", "Supply Fan 3C Velocity Pressure", "Fan_Reading.AirVelocityPressure")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sf2_vel_press", "Fan", "Supply Fan 3B Velocity Pressure", "Fan_Reading.AirVelocityPressure")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sf1_vel_press", "Fan", "Supply Fan 3A Velocity Pressure", "Fan_Reading.AirVelocityPressure")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("rf1_vel_press", "Fan" , "Return Fan 3A Velocity Pressure", "Fan_Reading.AirVelocityPressure")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("rf4_cfm_tnd", "Fan", "Return Fan 4 CFM", "Fan_Reading.AirVelocityCFM")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("rf3_cfm_tnd", "Fan", "Return Fan 3 CFM", "Fan_Reading.AirVelocityCFM")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("rf2_cfm_tnd", "Fan", "Return Fan 2 CFM", "Fan_Reading.AirVelocityCFM")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("rf1_cfm_tnd", "Fan", "Return Fan 1 CFM", "Fan_Reading.AirVelocityCFM")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("rf_cfm_tnd", "Fan", "Return Fan CFM", "Fan_Reading.AirVelocityCFM")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("rf4_vel_press", "Fan", "Return Fan 3D Velocity Pressure", "Fan_Reading.AirVelocityPressure")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("rf3_vel_press", "Fan", "Return Fan 3C Velocity Pressure", "Fan_Reading.AirVelocityPressure")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("rf2_vel_press", "Fan", "Return Fan 3B Velocity Pressure", "Fan_Reading.AirVelocityPressure")

#AHU
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m045", "AHU", "Number of Zones Requiring Cooling", "Air_Handling_Unit_Reading.CoolingRequest")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ahu/cl_stpt_tn", "AHU", "Cooling Setpoint", "Air_Handling_Unit_Reading.CoolingSetpoint")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m044", "AHU", "Number of Zones Requiring Heating", "Air_Handling_Unit_Reading.HeatingRequest")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ahu/ht_stpt_tn", "AHU", "Heating Setpoint", "Air_Handling_Unit_Reading.HeatingSetpoint")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("econ_stpt_tn", "AHU", "Economizer Setpoint", "Air_Handling_Unit_Reading.EconomizerSetpoint")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ma_temp", "AHU", "Mixed Air Temp", "Air_Handling_Unit_Reading.MixedAirTemperature")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("oa_temp", "AHU", "Outside Air Temp", "Air_Handling_Unit_Reading.OutsideAirTemperature")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m041", "AHU", "Occupied Mode", "Air_Handling_Unit_Reading.OccupiedMode")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("osa_co2", "AHU", "Outside Air Co2", "Air_Handling_Unit_Reading.OutsideAirCO2")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("osa_cfm", "AHU", "Outside Air Cfm", "Air_Handling_Unit_Reading.OutsideAirCFM")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("co2_stpt_tn", "AHU", "Return Air Co2 Setpoint", "Air_Handling_Unit_Reading.ReturnAirCO2Setpoint")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ra_co2", "AHU", "Return Air Co2", "Air_Handling_Unit_Reading.ReturnAirCO2")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ra_temp", "AHU", "Return Air Temperature", "Air_Handling_Unit_Reading.ReturnAirTemperature")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m798", "AHU", "Static Pressure Smoothed", "Air_Handling_Unit_Reading.StaticPressureSmoothed")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m403", "AHU", "Static SP", "Air_Handling_Unit_Reading.StaticSP")
# Zone 3
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sa_temp", "AHU", "Supply Temperature", "Air_Handling_Unit_Reading.SupplyAirTemperature")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("st_press1", "AHU", "Static Pressure 2 A", "Air_Handling_Unit_Reading.StaticPressure")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("sa_stpt_tn", "AHU", "Supply Air Set Point", #"Can't find in database")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ra_sp", "AHU" , "Return Air Static Pressure", "Air_Handling_Unit_Reading.StaticPressure")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("osacfm", "AHU", "Outside Air CFM", "Air_Handling_Unit_Reading.OutsideAirCFM")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("oa_temperature", "AHU", "Outside Air Temperature", "Air_Handling_Unit_Reading.OutsideAirTemperature")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("ht_stpt_tn", "AHU", "Heat Setpoint", "Air_Handling_Unit_Reading.HeatingSetpoint")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("cl_stpt_tn", "AHU", "Cooling Setpoint", "Air_Handling_Unit_Reading.CoolingSetpoint")

#VAV
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("vav/cl_stpt_tn", "VAV", "Cooling Setpoint", "Variable_Air_Volume_Reading.CoolingSetpoint")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("vav/ht_stpt_tn", "VAV", "Heating Setpoint", "Variable_Air_Volume_Reading.HeatingSetpoint")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("da_temp", "VAV", "Discharge Temperature", "Variable_Air_Volume_Reading.DischargeTemperature")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("dmpr_pos_tn", "VAV", "Damper Position", "Variable_Air_Volume_Reading.DamperPosition")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("st_press", "VAV", "Duct Static Pressure", "Variable_Air_Volume_Reading.DuctStaticPressure")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("flow_input", "VAV", "Flow Control/Flow Input", "Variable_Air_Volume_Reading.FlowInput")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m311", "VAV", "Zone Temperature", "Variable_Air_Volume_Reading.ZoneTemperature")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("m211", "VAV", "Static Setpoint 1", "Variable_Air_Volume_Reading.DuctStaticPressure")

#VFD
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("speed_rpm_1617_tn", "VFD", "1617 Speed RPM", "VFD_Reading.SpeedRPM")
insert into PathMappings (Path, ComponentType, Description, DatabaseMapping) values ("power_kw_1610_tn", "VFD", "1610 Power Kw", "VFD_Reading.PowerKW")
