#! /usr/sbin/python

# Craig Cutforth
# LmwaParser.py
# Created: 2018.04.27

import os
import time
import csv

def convertFileToDict(fhandle):
    for line in fhandle:
        print(line)
    print("=============DONE============")


BitField15 = "TBD"
BitField14 = "Burst 9-24 hours within last 30 days"
BitField13 = "Burst 1-8 hours within last 30 days"
BitField12 = "TBD"
BitField11 = "TBD"
BitField10 = "TBD"
BitField9 = "TBD"
BitField8 = "TBD"
BitField7 = "TBD"
BitField6 = "TBD"
BitField5 = "TBD"
BitField4 = "TBD"
BitField3 = "TBD"
BitField2 = "TBD"
BitField1 = "TBD"
BitField0 = "TBD"

Fieldnames = ['Meter Serial Number', 'Meter Reading', 'Consumption Type' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ,'' , 'Volume', 'Volume Units', 'Operating Time', 'Operating Time Units']

InputFile = "20180401_DLC_NoWells.csv"
# fileHandle = open(InputFile)
# print(fileHandle)
# convertFileToDict(fileHandle)
#
# with open(InputFile,'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
#
# print("=============Now DictReader============")

with open(InputFile,'rt') as CsvFileHandle:
    reader = csv.DictReader(CsvFileHandle,fieldnames=Fieldnames,delimiter=';')
    for row in reader:
        print(row['Meter Serial Number'], row['Meter Reading'], )
