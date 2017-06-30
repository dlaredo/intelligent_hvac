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

#Thermafusers
insert into ComponentRelationships (ComponentName, ParentComponent, Group) values ("1C1A", "Hallway 1C1 VAV-1-20", NULL);