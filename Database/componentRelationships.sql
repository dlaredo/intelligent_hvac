use HVAC;

#AHU
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("AHU-4", NULL, 1);

#VAVs
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Breakout 120J VAV-1-23", "AHU-4", 4);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Computation 120A&B VAV-1-25", "AHU-4", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Conference 224 VAV-2-26", "AHU-4", 2);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Conference 301 VAV-3-22", "AHU-4", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Conference 324 VAV-3-26", "AHU-4", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("CSE Break Out 213A VAV-2-34", "AHU-4", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("CSE Lab 206 VAV-2-38", "AHU-4", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("CSE Storage & Soldering 218 & 219 VAV-2-31", "AHU-4", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Engineering 315, Reception 315A VAV-3-35", "AHU-4", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Hallway 0C6 VAV-B-36", "AHU-4", 5);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Hallway 1C1 VAV-1-20", "AHU-4", 3);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Hallway 1C6 VAV-1-19", "AHU-4", 3);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Hallway 213 VAV-2-36", "AHU-4", 5);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Hallway 2C1,6,7 VAV-2-25", "AHU-4", 3);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Hallway 2C2 & 3 VAV-2-35", "AHU-4", 5);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Hallway 2C4, Office 221 VAV-2-28", "AHU-4", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Hallway 2C5 VAV-2-24", "AHU-4", 3);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Hallway 3C1,5,6,7 VAV-3-23", "AHU-4", 3);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Hallway 3C4, Conference Support 325  VAV-3-25", "AHU-4", 2);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Office 120E-H VAV-1-24", "AHU-4", 4);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Office 205 VAV-2-39", "AHU-4", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Office 207-217 VAV-2-30", "AHU-4", 4);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Office 222 & 223 VAV-2-27", "AHU-4", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Office 305 VAV-3-30", "AHU-4", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Office 305A, 310A-C, 315E-G VAV-3-36", "AHU-4", 4);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Office 310 D,E Lactaion 312 VAV-3-31", "AHU-4", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Office 315H VAV-3-37", "AHU-4", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Office 321, 322, 323 VAV-3-33", "AHU-4", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Office Support 315B & C VAV-3-32", "AHU-4", 4);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Printers 120C VAV-1-21", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Research Equip. 001 VAV-B-34", "AHU-4", -1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Research Equip. 120D VAV-1-22", "AHU-4", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Research Group 1-3 213C-E VAV-2-33", "AHU-4", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Research Group 4 213B VAV-2-37", "AHU-4", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Research Group 5 213F VAV-2-32", "AHU-4", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Research Group 6 311 VAV-3-29", "AHU-4", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Research Group 7 313 VAV-3-28", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Research Group 8 314 VAV-3-27", "AHU-4", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Scholarly Activity 102 VAV-1-18", "AHU-4", 2);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Scholarly Activity 220 VAV-2-29", "AHU-4", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Scholarly Activity 320  VAV-3-34", "AHU-4", 1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Vending 002 VAV-B-35", "AHU-4", -1);
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("Video Conference 302 VAV-3-24", "AHU-4", 2);

#Thermafusers
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("1C1A", "Hallway 1C1 VAV-1-20", NULL);