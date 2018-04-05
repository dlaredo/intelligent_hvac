import csv
#from sets import Set
#
with open ('deviceListDump.csv', 'r') as d, open ('pointListBacnet.csv') as p:
    with open('map3.csv','w') as t, open ('unmap3.csv','w') as n :
        reader = csv.reader(d)
        reader2 = csv.reader(p)  
        writer = csv.writer(t)
        writer2 = csv.writer(n)
        
        #list1 = list(reader)
        dict1 = dict ()
        set2 = set()
        set3 = set()
        writer.writerow (['Address','DeviceId','DeviceName'])
        writer2.writerow(['DeviceId','DeviceName'])
        #for row in reader:
        it = iter(reader)
        next(it, None)  # skip first item.
        for row in it:
            
            deviceID = row[1]
            deviceID = deviceID.strip() #get rid off blank space before each entry
           
            dict1.update({deviceID:row[0]}) #deviceId and Device address are in a dict
            #set3.add({deviceID,})
        #print (dict1)
           
        it = iter(reader2)
        next(it, None)  # skip first item.
        for row in it:
           if len(row) >= 6:
  
                deviceID = row[6]
                deviceID = deviceID.split(':')[1]
    
                deviceID = deviceID.strip()
        #check wheather they have overlap deviceid
                if deviceID in dict1:
                    #print (deviceID)
                    deviceName = row[-1]
                    deviceName = deviceName.split('/')[0]
                    
                    if deviceName not in set2: #stops repeating device ids
                        
                        set2.add(deviceName)
                        
                        writer.writerow([dict1[deviceID], deviceID,deviceName])
                # check the deviceid is not existed in dumplist       
                else: 
                    if deviceID not in set3:
                        set3.add(deviceID)
                        deviceName = row[-1]
                        deviceName = deviceName.split('/')[0]
                        writer2.writerow([deviceID,deviceName])
                    
                        #print (dict1[deviceID], deviceID,deviceName)
                        
                #
                    
                    
#           
#            set1.add(deviceID)
            
            
           
           
        

    