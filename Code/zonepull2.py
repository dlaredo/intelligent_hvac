#WELCOME TO THE ZONEPULL SCRIPT
#ONLY 4 THINGS SHOULD BE MODIFIED
#
#
#
#
#
#
#
#
#
#
def format_data(startTime, endTime, serverSP, path):

    print(startTime.strftime("%m/%d/20%y %I:%M:%S %p"))
    print(endTime.strftime("%m/%d/20%y %I:%M:%S %p"))

    data = serverSP.service.getTrendData('soap',"", path, startTime.strftime("%m/%d/20%y %I:%M:%S %p"), endTime.strftime("%m/%d/20%y %I:%M:%S %p"), False, 0)
    tStmps = []
    values = []
    tStamp = []
    vals = []
    #print data


    # SEPERATE DATA INTO TWO ARRAYS: TIME STAMPS AND VALUE

    for k in range(0,len(data),2):
        tmpDate = datetime.datetime.strptime(data[k],"%m/%d/20%y %I:%M:%S %p")
        tStmps.append(tmpDate)
        values.append(float(data[k+1]))
    tStamp = None
    vals = None

    print(len(tStmps))
    return values,vals,tStmps,tStamp,data
############################################################################################################################################################################################################################################################################################################
def getdata(path,cprog,point,date,d):
    print(cprog)
    server= "10.20.0.47"
    host = 'http://'+server+'/_common/services/TrendService?wsdl'
    serverSP = zeep.Client(wsdl=host)
    #serverSP = SOAPpy.SOAPProxy(host)
    #serverPt = SOAPpy.SOAPProxy('http://'+server+'/_common/services/EvalService?wsdl')


    today = datetime.date.today()

    #SET YEAR, MONTH HERE!!<<<<---------------------------------------------------------------

    custdate = datetime.date(2017,4,d)
    print("custdate " + custdate.strftime('%m/%d/%Y'))

    #SET MONTH HERE!!<<<<---------------------------------------------------------------

    filedate= custdate-timedelta(1,0,0,0,0,0,0)
    print("filedate " + filedate.strftime('%m/%d/%Y'))


    moment = time.min

    end = datetime.datetime.combine(custdate, moment)
    print("end " + end.strftime('%m/%d/%Y %H:%M:%S'))

    endTime = end
    print(endTime)
    startTime  = endTime - timedelta(1,0,0,0,0,0,0)
    print("start " + startTime.strftime('%m/%d/%Y %H:%M:%S'))

    #print endTime
    #print startTime
    print(cprog)
    global values
    varray=[]
    a="time"
    #b=path

    # How many seconds in total
    dt = (endTime-startTime)
    print(dt)
    daySec = dt.days*24*3600
    sec = dt.seconds

    totalSecs = daySec + sec

    print(totalSecs)

    # time in 5 minute slots
    global numSlots

    numSlots = int(totalSecs/(60*5))

    delta = timedelta(0,0,0,0,5,0,0)



    #Make folder for new date ,and control program

    if not os.path.exists('Desktop/hvac_data_test/Zone4/'+cprog+''):
        os.makedirs('Desktop/hvac_data_test/Zone4/'+cprog+'')


    #Wu's Per Time Stamp Method writes one time stamped row at a time and pulls each value from the bacnetrend; proven but very. very. slow.

    #FILE = open('/Users/Student/Dropbox/HVAC/Data/Zone44444/'str(startTime)'+"-"+'str(custdate)+'/'+cprog+' '+str(yesterday)+'.csv','w')
    #FILE.write(""+str(a)+","+str(b)+"\n")


    # for i in range(0,numSlots):
    #
    #       curr = startTime+delta*i
    #       last=curr+delta
    #       row = curr.strftime("%m%d20%y %H%M%S")+"\t"
    #       for j in range(0,len(path),1):
    #           try:
    #               print path[j]
    #               data = format_data(curr, last, serverSP, path[j])
    #           except:
    #
    #               print "wtf is going on"
    #               continue
    #
    #           print data
    #
    #           if (len(data)>=2):
    #               if data[1]==-1:
    #                   data[1]=" "
    #               row = row+data[1]+"\t"
    #           else:
    #               row = row+"-1\t"
    #           print row[:-1]
    #       FILE.write(row+"\n")
    #   FILE.close()




#Attempting to pull day's worth of data, then appending to csv
#tStmps=[]


    tStmp=[]

##USED THIS TO HARDCODE TIMESTAMPS: NOT SAFE!

    for h in range (0,numSlots,1):
        start=startTime+timedelta(0,0,0,0,5,0,0)
        next=start+timedelta(0,0,0,0,5*h,0,0)
        tStmp.append(next)


    M = np.empty(shape=(numSlots, len(path)), dtype=float)
    M.fill(-1)
    for j in range(0,len(path),1):

        try:
            print(path[j])
            b=path[j]
            values,vals,tStmps,tStamp,data = format_data(startTime,endTime, serverSP, path[j])


        except:

            print("wtf is going on")
            continue





        if len(tStmps)==0:
            print("empty array")
            continue




        print(tStmps)
        print(values)

        if len(tStmps)==len(tStmp):


            try:
                print(values)
                M[:,j]=(values)
            except:

                print("dimension problem, check timestamps")

                continue


        else:



            print("Initiate WU TANG STYLE for "+path[j])
            for h in range (0,len(tStmp),1):
                start=startTime+timedelta(0,0,0,0,5,0,0)
                next=start+timedelta(0,0,0,0,5*h,0,0)
                for t in range(0,len(tStmps),1):
                    delt=next-tStmps[t]
                #print next
                    if delt.total_seconds()<0:
                    #print "HEYYYYYYYYYYYYYYYYYY"
                    #print delt
                    #print tStmps[t]
                        continue
                    elif delt.total_seconds()==0:
                        #print "THIS IS A MATCH!!!"
                        M[h,j]=values[t]
                        break
                    else:
                        #print "THERE SEEMS TO BE A MISTAKE"
                        continue
        print(M[:,j])




# Formatting CSV
#print M
    a= "Time"
    b= str(path)

    FILE = open('Desktop/hvac_data_test/Zone4/'+cprog+'/'+cprog+' '+str(filedate)+'.csv','w')
    FILE.write(str(a)+","+str(b)+'\n')

    for f in range(0,len(tStmp),1):

        FILE.write(str(tStmp[f])+",")
        for a in range(0,len(path),1):
            FILE.write(str(M[f,a])+",")
        FILE.write('\n')



#np.savetxt('/Users/Student/Dropbox/HVAC/Data/Zone4/'+cprog+'/'+cprog+' '+str(filedate)+'.csv', str(row_label) + M, delimiter=",",fmt='%10.5f')



    FILE.close()
    return 1


############################################################################################################################################################################################################################################################################################################

import zeep
import sys, time, calendar
import smtplib
import math
from time import  localtime, strftime, sleep, strptime
from datetime import datetime,timedelta, date, time
from pylab import *
import csv
import numpy as np
from collections import defaultdict
import os
import string

print(datetime.datetime.now())
from datetime import date, timedelta
global yesterday
yesterday = date.today() - timedelta(1)
print(yesterday)
date=yesterday.strftime('%m-%d-%y')
np.set_printoptions(threshold=np.inf)


# a dictionary whose value defaults to a list.
stuff = defaultdict(list)

# open the csv file and iterate over its rows. then enumerate()
# function gives us an incrementing row number

for i, row in enumerate(csv.reader(open('Zone4.csv', 'r'))):

    # skip the header line and any empty rows
    # we take advantage of the first row being indexed at 0
    # i=0 which evaluates as false, as does an empty row

    if not i or not row:
        continue
    # unpack the columns into local variables


    serv,loc,branch,sub,cprog,point,path = row


    # for each room, add the trend to the list


    stuff[cprog].append(path)

# loop over each room and its list of trends and get trends for each room
# d may be adjusted to pull specific time range( make sure to change the month if needed in custdate)


#SET DATE RANGE HERE!! (MAKE SURE YOU PUT THE DAY AFTER DATE OF INTEREST eg:Dec 9 = 10 <<<<---------------------------------------------------------------

for d in range(1,11,1):
    for cprog,path in stuff.items():
        print(cprog, path)
        #wait = input("PRESS ENTER TO CONTINUE.")

        test=getdata(path,cprog,point,date,d)

        if (test==1):

            print("suuhhdude")

        else:
            print("no data from path")
