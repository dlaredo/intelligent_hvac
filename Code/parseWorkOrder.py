from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd

from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

import xlsxwriter
import dateutil.parser as dparser
import datefinder
import datetime

# problem vocab ['found',]
# cause vocab ['stuck','reset']
#column names: Workorder #, Date, endDate Involved Comp (AHU, SAV,...), Location ID, Resquest
#   Issues, Raw data (all the comments. Each comment is a list)

#date- starting date and ending date
#paramter in console
#end date put empty

file = r'WO-1030_SE2_HVAC_WO636713604036759879.xls'
df = pd.read_excel(file,header = 6)

#raw data coloumn
def rawDataCol():
    n =0
    commentlist = list()
    for i in range(1,len(df)):
        #find the same workorder group
        if type(df['Work Order #'][i])!= str and type(df['Work Order #'][i-1]) == str\
         or i == (len(df)-2):
            #find all the comments for specific work order
            commtemp =list()
            for j in range(n,i+1):
                if df['Work Order #'][j] == 'Comment':
                    commtemp.append(df.loc[j][2])
                    n = i
            commentlist.append(commtemp)
    return commentlist

#start date col
def dateCol():

    datelist = list()
    for d in range(len(df)):
        if type(df['Request Date'][d] )== datetime.datetime:
            datelist.append(df['Request Date'][d])
    return datelist

#end date col
def endDateCol():

    raw = rawDataCol()
    endDateList = list()
    d = dateCol()
    tempL = list()

    if len(raw[line]) == 0:
        maxD = ''
    else:
        for l in range(len(raw[line])):
            matches = list(datefinder.find_dates(raw[line][l]))
            if matches[0] > maxD:
                maxD = matches[0]
        tempL.append(maxD)
    return tempL

#work order as key
def workOrderCol():
    orderlist = list()
    for w in range (len(df)):
        if type(df['Work Order #'][w])== str and df['Work Order #'][w].startswith( 'PP' ):
            orderlist.append(df['Work Order #'][w])
    return orderlist

#find component in request col
def componentColRequest():
    compoentlist = ['thermofuse','a/h#3','air handlers','hot water valve'\
    ,'therma-fuser','ahu 7','vfd','filter','sav','ahu','variabl air volume','vav'\
    ,'fan','damper','coil','staged air volume','a/h-4','valve','thermofusser','static pressure'\
    ,'a/c','belts']

    colist = list()
    for e in range (len(df)):
        if type(df['Request Date'][e]) == str:
            co2list = list()
            for co in compoentlist:
                if co in df['Request Date'][e].lower():
                    co2list.append(co)
            colist.append(co2list)
    return colist

#find compoent in comment col
def componetColComment():
    compoentlist = ['thermofuse','a/h#3','air handlers','hot water valve'\
    ,'therma-fuser','ahu 7','vfd','filter','sav','ahu','variabl air volume','vav'\
    ,'fan','damper','coil','staged air volume','a/h-4','valve','thermofusser','static pressure'\
    ,'a/h#4','belts']

    colist = list()
    commentL= rawDataCol()
    for e in commentL:
        tempL = list()
        for l in e:
            for co in compoentlist:
                if co in l.lower():
                    tempL.append(co)
                tempL = set(tempL)
                tempL = list(tempL)

        colist.append(tempL)

    return colist

#combine requests
def compoentCombo():
    CC = componetColComment()
    com = componentColRequest()
    InvolvedCom = [x+y for x, y in zip(CC,com )]
    for i in range(len(InvolvedCom)):
        s = set (InvolvedCom[i])
        InvolvedCom[i] = list(s)
    return InvolvedCom

#find locaitn of the issues
def locationID():
    loclist = list()
    for i in range (len(df)):
        if type(df['Location ID'][i])== str:
            loclist.append(df['Location ID'][i])
    return loclist

#give initial request
def requestCol():
    relist = list()
    for i in range (len(df)):
        if type(df['Request Date'][i])== str:
            relist.append(df['Request Date'][i])
    return relist

#extact issues
def issueCol():
    issueList = ['found','found out']
    raw = rawDataCol()

    colist = list()

    for e in raw:
        tempL = list()
        seen = list()
        for l in e:
            for co in issueList:
                if co in l.lower():
                    if l[-20:-5] not in seen:
                        seen.append(l[-20:-5])
                        tempL.append(l)
        colist.append(tempL)
    return colist


iss = issueCol()
loc = locationID()
re = requestCol()
InvolvedCom = compoentCombo()
d = dateCol()
r =rawDataCol()
w = workOrderCol()
end = endDateCol()

# #testFinalList
match_dc = [[a, b, c, d, e, f, g] for a, b, c, d, e, f, g in zip(d, end, InvolvedCom, loc, re,\
iss, r)]

#make dictonary for workorder and all the rest coloumns
newdic = {}

for l in range(len(w)):
    newdic[w[l]] = match_dc[l]

print(newdic['PP-1042597'])


