use HVAC;

#Insert ghost AHU (AHU-1/AHU-2)
insert into Air_Handling_Unit (AHUNumber, AHUName) values (1, "AHU-1/AHU-2");

#AHU
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("AHU-1", NULL, "AHU", 7);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("AHU-2", NULL, "AHU", 7);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("AHU-3", NULL, "AHU", 7);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("AHU-4", NULL, "AHU", 7);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("AHU-5", NULL, "AHU", 7);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("AHU-6", NULL, "AHU", 7);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("AHU-7", NULL, "AHU", 7);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("AHU-1/AHU-2", NULL, "AHU", 7);

#SAV
#Basement
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Microtome 090F SAV-B1-A","AHU-1/AHU-2","SAV",6); #2 AHU control this SAV
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Prep 090G SAV-B2-C", "AHU-1/AHU-2","SAV",6); #2 AHU control this SAV
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Imaging 090 SAV-B3-B", "AHU-1/AHU-2","SAV",6 );#2 AHU control this SAV
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Training 090E SAV-B4-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("SEM 090D SAV-B5-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Titan 090B North SAV-B6-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Dual Beam 090A SAV-B7-B", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Titan 090B South SAV-B8-B", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Pump 085 SAV-B9-B", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("TEM 090C SAV-B10-B", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Instrument 080G SAV-B11-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Instrument 080F SAV-B12-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Equipment 080C SAV-B14-B", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Instrument 080E SAV-B15-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Instrument 080D SAV-B16-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Hallway 0C9 SAV-B17-C", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Computation 080A SAV-B19-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Laser lab 070 SAV-B20-B", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Material Science 080B SAV-B21-E", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Visualization 060 SAV-B22-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("CER 50H SAV-B23-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Support 050G SAV-B24-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Equipment 050D SAV-B25-B", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Instrument 050F SAV-B26-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Support 050A SAV-B29-B", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Instrument 050C SAV-B30-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Computation 050B SAV-B31-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Equipment 050E SAV-B32-B", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Server Tech 030 SAV-B33-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Mass Spec 024 SAV-B37-D", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("NMR Pumps 020C SAV-B38-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("NMR Mass 020 SAV-B-39", "AHU-1/AHU-2","SAV",6);
#First Floor
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Wind Tunnel 185 West SAV-1A1-C", "AHU-1/AHU-2","SAV",6); # multiple AHU used for this SAV
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Wind Tunnel 185 East SAV-1A2-C", "AHU-1/AHU-2","SAV",6); #multiple AHU used for this SAV
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Instructor Support 190 SAV-1A3-B", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Thermofluid Lab 180 SAV-1A4-C", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Prep 170 SAV-1A5-C", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Wet Lab 160 West SAV-1A6-C", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Wet Lab 160 East SAV-1A7-C", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Machine Shop 175 SAV-1A8-C", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Learning 165 West SAV-1B9-C", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Learning 165 East SAV-1B10-C", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Wet Lab 150 West SAV-1B11-C", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Wet Lab 150 East SAV-1B12-C", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Prep 140 SAV-1B13-C", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Wet Lab 130 West SAV-1B14-C", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Wet Lab 130 East SAV-1B15-C", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Electronics 155 SAV-1B16-C", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Tech Office 135 SAV-1B17-CA", "AHU-1/AHU-2","SAV",6);

#second floor
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Breakout 290 SAV-2A1-C", "AHU-1/AHU-2","SAV",6); 
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Offices 291-293 SAV-2A2-C", "AHU-1/AHU-2","SAV",6); 
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Computation 230Q SAV-2A3-A", "AHU-1/AHU-2","SAV",6); # multiple AHU used for this SAV
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Mech. Enginnering 230P SAV-2A4-A", "AHU-1/AHU-2","SAV",6); #multiple AHU used for this SAV
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Mech. Engineering 230N SAV-2A5-C", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Office 265 SAV-2A6-CA", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Mech. Enginnering 230M SAV-2A7-B", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Mech. Engineering 230R  SAV-2A8-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Mech Engineering 230K SAV-2A9-B", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Hallway 230 SAV-2A10-C", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Hallway 2C9 SAV-2A11-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Mech. Engineering 230S SAV-2A12-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Mech. Engineering 230J SAV-2A13-B", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Mech. Engineering 230T SAV-2A14-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Mech. Engineering 230H SAV-2A15-C", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Mech. Engineering 230F SAV-2A16-B", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Hallway 230 SAV-2A17-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Mech. Engineering 230U SAV-2A18-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Mech. Engineering 230E SAV-2A19-D", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Mech. Engineering 230V SAV-2A20-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Mech. Engineering 230D SAV-2A21-C", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Mech. Engineering 230C SAV-2A22-A", "AHU-1/AHU-2","SAV",6);

#third floor
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Breakout 390 SAV-3A1-C", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Offices 391-393 SAV-3A2-C", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Office Support 365 SAV-3A3-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Instrument 340P SAV-3A4-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Instrument 340R SAV-3A5-B", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Instrument 340Q SAV-3A6-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Instrument 340N SAV-3A7-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Bioengineering 340 West SAV-3A8-E", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Cell Culture 340L SAV-3A9-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Cell Culture 340J SAV-3A10-B", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Hallway 3C9 SAV-3A11-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Cell Culture 340H SAV-3A12-B", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Bioengineering 340 Center SAV-3A13-E", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Cell Culture 340G SAV-3A14-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Autoclave 355 SAV-3A15-B", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Cell Culture 340F SAV-3A16-B", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Cell Culture 340C SAV-3A17-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Bioengineering 340 East SAV-3A18-E", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Instrument 340D SAV-3A19-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Instrument 340B SAV-3A20-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Organic Chemistry 335 SAV-3A21-A", "AHU-1/AHU-2","SAV",6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Organic Chemistry 330  3A22", "AHU-1/AHU-2","SAV",6);





#VAVs
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Breakout 120J VAV-1-23", "AHU-4", "VAV", 4);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Computation 120A&B VAV-1-25", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Conference 224 VAV-2-26", "AHU-4", "VAV", 2);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Conference 301 VAV-3-22", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Conference 324 VAV-3-26", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("CSE Break Out 213A VAV-2-34", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("CSE Lab 206 VAV-2-38", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("CSE Storage & Soldering 218 & 219 VAV-2-31", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Engineering 315, Reception 315A VAV-3-35", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Hallway 0C6 VAV-B-36", "AHU-4", "VAV", 5);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Hallway 1C1 VAV-1-20", "AHU-4", "VAV", 3);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Hallway 1C6 VAV-1-19", "AHU-4", "VAV", 3);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Hallway 213 VAV-2-36", "AHU-4", "VAV", 5);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Hallway 2C1,6,7 VAV-2-25", "AHU-4", "VAV", 3);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Hallway 2C2 & 3 VAV-2-35", "AHU-4", "VAV", 5);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Hallway 2C4, Office 221 VAV-2-28", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Hallway 2C5 VAV-2-24", "AHU-4", "VAV", 3);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Hallway 3C1,5,6,7 VAV-3-23", "AHU-4", "VAV", 3);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Hallway 3C4, Conference Support 325  VAV-3-25", "AHU-4", "VAV", 2);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Office 120E-H VAV-1-24", "AHU-4", "VAV", 4);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Office 205 VAV-2-39", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Office 207-217 VAV-2-30", "AHU-4", "VAV", 4);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Office 222 & 223 VAV-2-27", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Office 305 VAV-3-30", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Office 305A, 310A-C, 315E-G VAV-3-36", "AHU-4", "VAV", 4);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Office 310 D,E Lactaion 312 VAV-3-31", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Office 315H VAV-3-37", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Office 321, 322, 323 VAV-3-33", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Office Support 315B & C VAV-3-32", "AHU-4", "VAV", 4);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Printers 120C VAV-1-21", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Research Equip. 001 VAV-B-34", "AHU-4", "VAV", 6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Research Equip. 120D VAV-1-22", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Research Group 1-3 213C-E VAV-2-33", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Research Group 4 213B VAV-2-37", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Research Group 5 213F VAV-2-32", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Research Group 6 311 VAV-3-29", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Research Group 7 313 VAV-3-28", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Research Group 8 314 VAV-3-27", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Scholarly Activity 102 VAV-1-18", "AHU-4", "VAV", 2);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Scholarly Activity 220 VAV-2-29", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Scholarly Activity 320  VAV-3-34", "AHU-4", "VAV", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Vending 002 VAV-B-35", "AHU-4", "VAV", 6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Video Conference 302 VAV-3-24", "AHU-4", "VAV", 2);


#Thermafusers
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("1C1A", "Hallway 1C1 VAV-1-20", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("1C1B", "Hallway 1C1 VAV-1-20", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("1C1C", "Hallway 1C1 VAV-1-20", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("1C6A", "Hallway 1C6 VAV-1-19", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("1C6B", "Hallway 1C6 VAV-1-19", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("1C6C", "Hallway 1C6 VAV-1-19", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("1C6D", "Hallway 1C6 VAV-1-19", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("2C1A", "Hallway 2C1,6,7 VAV-2-25", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("2C1B", "Hallway 2C1,6,7 VAV-2-25", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("2C3-1", "Hallway 2C2 & 3 VAV-2-35", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("2C3-2", "Hallway 2C2 & 3 VAV-2-35", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("2C4", "Hallway 2C4, Office 221 VAV-2-28", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("2C5", "Hallway 2C5 VAV-2-24", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("2C6A", "Hallway 2C1,6,7 VAV-2-25", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("2C6B", "Hallway 2C1,6,7 VAV-2-25", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("2C6C", "Hallway 2C1,6,7 VAV-2-25", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("2C6D", "Hallway 2C1,6,7 VAV-2-25", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("2C6E", "Hallway 2C1,6,7 VAV-2-25", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("3C1-A", "Hallway 3C1,5,6,7 VAV-3-23", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("3C1-B", "Hallway 3C1,5,6,7 VAV-3-23", "Thermafuser", NULL);

insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("3C2", "Office 310 D,E Lactaion 312 VAV-3-31", "Thermafuser", NULL);

insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("3C4", "Hallway 3C4, Conference Support 325  VAV-3-25", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("3C6-A", "Hallway 3C1,5,6,7 VAV-3-23", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("3C6-B", "Hallway 3C1,5,6,7 VAV-3-23", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("3C6-C", "Hallway 3C1,5,6,7 VAV-3-23", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("3C6-D", "Hallway 3C1,5,6,7 VAV-3-23", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Bridge 2C7-1", "Hallway 2C1,6,7 VAV-2-25", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Bridge 2C7-2", "Hallway 2C1,6,7 VAV-2-25", "Thermafuser", NULL);

#Check this one
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Research Cooridor", "Office 310 D,E Lactaion 312 VAV-3-31", "Thermafuser", NULL);

insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room 102A-1", "Scholarly Activity 102 VAV-1-18", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room 102A-2", "Scholarly Activity 102 VAV-1-18", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room 102A-3", "Scholarly Activity 102 VAV-1-18", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room 102A-4", "Scholarly Activity 102 VAV-1-18", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room 102A-5", "Scholarly Activity 102 VAV-1-18", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-001", "Research Equip. 001 VAV-B-34", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-002", "Vending 002 VAV-B-35", "Thermafuser", NULL);

insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-0C1", "Hallway 0C6 VAV-B-36", "Thermafuser", NULL);

insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-0C6A", "Hallway 0C6 VAV-B-36", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-0C6B", "Hallway 0C6 VAV-B-36", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-120A-1", "Computation 120A&B VAV-1-25", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-120A-2", "Computation 120A&B VAV-1-25", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-120A-3", "Computation 120A&B VAV-1-25", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-120B-1", "Computation 120A&B VAV-1-25", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-120B-2", "Computation 120A&B VAV-1-25", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-120B-3", "Computation 120A&B VAV-1-25", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-120C", "Printers 120C VAV-1-21", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-120D", "Research Equip. 120D VAV-1-22", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-120E", "Office 120E-H VAV-1-24", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-120F", "Office 120E-H VAV-1-24", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-120G", "Office 120E-H VAV-1-24", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-120H-1", "Office 120E-H VAV-1-24", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-120H-2", "Office 120E-H VAV-1-24", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-120J-1", "Breakout 120J VAV-1-23", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-120J-2", "Breakout 120J VAV-1-23", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-205", "Office 205 VAV-2-39", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-206-1", "CSE Lab 206 VAV-2-38", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-206-2", "CSE Lab 206 VAV-2-38", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-207", "Office 207-217 VAV-2-30", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-208", "Office 207-217 VAV-2-30", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-209", "Office 207-217 VAV-2-30", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-210", "Office 207-217 VAV-2-30", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-211", "Office 207-217 VAV-2-30", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-212", "Office 207-217 VAV-2-30", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-213A", "CSE Break Out 213A VAV-2-34", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-213B-1", "Research Group 4 213B VAV-2-37", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-213B-2", "Research Group 4 213B VAV-2-37", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-213C-1", "Research Group 1-3 213C-E VAV-2-33", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-213C-2", "Research Group 1-3 213C-E VAV-2-33", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-213D-1", "Research Group 1-3 213C-E VAV-2-33", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-213D-2", "Research Group 1-3 213C-E VAV-2-33", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-213E-1", "Research Group 1-3 213C-E VAV-2-33", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-213E-2", "Research Group 1-3 213C-E VAV-2-33", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-213F-1", "Research Group 5 213F VAV-2-32", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-213F-2", "Research Group 5 213F VAV-2-32", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-214", "Office 207-217 VAV-2-30", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-215", "Office 207-217 VAV-2-30", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-216", "Office 207-217 VAV-2-30", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-217", "Office 207-217 VAV-2-30", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-218", "CSE Storage & Soldering 218 & 219 VAV-2-31", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-221", "Hallway 2C4, Office 221 VAV-2-28", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-222", "Office 222 & 223 VAV-2-27", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-223", "Office 222 & 223 VAV-2-27", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-301-A", "Conference 301 VAV-3-22", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-301-B", "Conference 301 VAV-3-22", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-302A", "Video Conference 302 VAV-3-24", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-302B", "Video Conference 302 VAV-3-24", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-305-A", "Office 305A, 310A-C, 315E-G VAV-3-36", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-305-B", "Office 305 VAV-3-30", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-305-C", "Office 305 VAV-3-30", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-305a", "Office 305 VAV-3-30", "Thermafuser", NULL);

insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-310", "Office 310 D,E Lactaion 312 VAV-3-31", "Thermafuser", NULL);

insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-310A", "Office 305A, 310A-C, 315E-G VAV-3-36", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-310B", "Office 305A, 310A-C, 315E-G VAV-3-36", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-310C", "Office 305A, 310A-C, 315E-G VAV-3-36", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-310D", "Office 310 D,E Lactaion 312 VAV-3-31", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-310E", "Office 310 D,E Lactaion 312 VAV-3-31", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-311-A", "Research Group 6 311 VAV-3-29", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-311-B", "Research Group 6 311 VAV-3-29", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-312", "Office 310 D,E Lactaion 312 VAV-3-31", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-313A", "Research Group 7 313 VAV-3-28", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-313B", "Research Group 7 313 VAV-3-28", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-314A", "Research Group 8 314 VAV-3-27", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-314B", "Research Group 8 314 VAV-3-27", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-315", "Engineering 315, Reception 315A VAV-3-35", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-315A", "Engineering 315, Reception 315A VAV-3-35", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-315B", "Office Support 315B & C VAV-3-32", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-315C", "Office Support 315B & C VAV-3-32", "Thermafuser", NULL);

insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-315D", "Office 310 D,E Lactaion 312 VAV-3-31", "Thermafuser", NULL);

insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-315E", "Office 305A, 310A-C, 315E-G VAV-3-36", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-315F", "Office 305A, 310A-C, 315E-G VAV-3-36", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-315G", "Office 305A, 310A-C, 315E-G VAV-3-36", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-315H-A", "Office 315H VAV-3-37", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-315H-B", "Office 315H VAV-3-37", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-321", "Office 321, 322, 323 VAV-3-33", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-322", "Office 321, 322, 323 VAV-3-33", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-323", "Office 321, 322, 323 VAV-3-33", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-325", "Hallway 3C4, Conference Support 325  VAV-3-25", "Thermafuser", NULL);
 
#Zone 3
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-270", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-271", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-272", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-273", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-274", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-275", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-276", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-277", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-278", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-279", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-280", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-281", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-282", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-283", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-284", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-285", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-286", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-370", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-371", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-372", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-373", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-374", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-375", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-376", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-377", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-378", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-379", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-380", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-381", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-382", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-383", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-384", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-385", "AHU-3", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-386", "AHU-3", "Thermafuser", NULL);

#Zone 1&2
#found in the csv file but not in alc
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Computation 230A SAV-2A23-C", "AHU-1/AHU-2", "SAV", 6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Engineering 050 East SAV-B28-E", "AHU-1/AHU-2", "SAV", 6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Engineering 050 West SAV-B27-E", "AHU-1/AHU-2", "SAV", 6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Material Science 080 East SAV-B18-E", "AHU-1/AHU-2", "SAV", 6);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Material Science 080 West SAV-B13-E", "AHU-1/AHU-2", "SAV", 6);


insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-291", "Offices 291-293 SAV-2A2-C", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-292", "Offices 291-293 SAV-2A2-C", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-293", "Offices 291-293 SAV-2A2-C", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-391", "Offices 391-393 SAV-3A2-C", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-392", "Offices 391-393 SAV-3A2-C", "Thermafuser", NULL);
insert into ComponentRelationships (ComponentName, ParentComponent, ComponentType, ComponentGroup) values ("Room-393", "Offices 391-393 SAV-3A2-C", "Thermafuser", NULL);














