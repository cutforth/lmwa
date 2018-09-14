#! /usr/sbin/python

# Craig Cutforth
# LmwaParser.py
# Created: 2018.04.27

import os
import time
import csv
import pdb;

def convertFileToDict(fhandle):
    for line in fhandle:
        print(line)
    print("=============DONE============")


BitField15 = "Dry Interval Bit2"
BitField14 = "Dry Interval Bit1"
BitField13 = "Dry Interval Bit0"
BitField12 = "Dry Interval Bit2"
BitField11 = "Dry Interval Bit1"
BitField10 = "Dry Interval Bit0"
BitField9  = "Dry Interval Bit2"
BitField8  = "Dry Interval Bit1"
BitField7  = "Dry Interval Bit0"
BitField6  = "Dry Interval Bit2"
BitField5  = "Dry Interval Bit1"
BitField4  = "Dry Interval Bit0"
BitField3  = "Burst Active"
BitField2  = "Leak Active"
BitField1  = "Reverse Active"
BitField0  = "Dry Active"

Field1 = 'Meter Serial Number'
Field2 = 'Date And Time'
Field3 = 'Consumption Type'
Field4 = ''
Field5 = ''
Field6 = ''
Field7 = ''
Field8 = ''
Field9 = ''
Field10 = ''
Field11 = ''
Field12 = 'Volume'
Field13 = 'Volume Units'
Field14 = 'Operating Time'
Field15 = 'Operating Time Units'
Field16 = ''
Field17 = ''
Field18 = ''
Field19 = ''
Field20 = ''
Field21 = ''
Field22 = ''
Field23 = ''
Field24 = ''
Field25 = ''
Field26 = ''
Field27 = ''
Field28 = 'InfoRegister'
Field29 = ''
Field30 = ''
Field31 = ''
Field32 = ''
Field33 = ''
Field34 = 'Historical Volume'
Field35 = 'Historical Volume Units'
Field36 = ''
Field37 = ''
Field38 = ''
Field39 = ''
Field40 = ''
Field41 = ''
Field42 = ''
Field43 = ''
Field44 = ''
Field45 = ''
Field46 = ''
Field47 = ''
Field48 = ''
Field49 = ''
Field50 = ''
Field51 = ''
Field52 = ''
Field53 = ''
Field54 = ''
Field55 = ''
Field56 = ''
Field57 = ''
Field58 = ''
Field59 = ''
Field60 = ''
Field61 = ''
Field62 = ''
Field63 = ''
Field64 = ''
Field65 = ''
Field66 = ''
Field67 = ''
Field68 = ''
Field69 = ''
Field70 = ''
Field71 = ''
Field72 = ''
Field73 = ''
Field74 = ''
Field75 = ''
Field76 = ''
Field77 = ''
Field78 = ''
Field79 = ''
Field80 = ''
Field81 = ''
Field82 = ''
Field83 = ''
Field84 = 'Revision'
Fieldnames = [Field1,  Field2,  Field3,  Field4,  Field5,
              Field6,  Field7,  Field8,  Field9,  Field10,
              Field11, Field12, Field13, Field14, Field15,
              Field16, Field17, Field18, Field19, Field20,
              Field21, Field22, Field23, Field24, Field25,
              Field26, Field27, Field28, Field29, Field30,
              Field31, Field32, Field33, Field34, Field35,
              Field36, Field37, Field38, Field39, Field40,
              Field41, Field42, Field43, Field44, Field45,
              Field46, Field47, Field48, Field49, Field50,
              Field51, Field52, Field53, Field54, Field55,
              Field56, Field57, Field58, Field59, Field60,
              Field61, Field62, Field63, Field64, Field65,
              Field66, Field67, Field68, Field69, Field70,
              Field71, Field72, Field73, Field74, Field75,
              Field76, Field77, Field78, Field79, Field80,
              Field81, Field82, Field83, Field84
              ]

InputFile = "2018.03.06 LMWA Readings.csv"
# InputFile = "20180401_DLC_NoWells.csv"
# InputFile = "2018.05.06 LMWA Readings.csv"
# InputFile = "2018.06.06 LMWA Readings.csv"
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
# pdb.set_trace()

with open(InputFile,'rt') as CsvFileHandle:
    reader = csv.DictReader(CsvFileHandle,fieldnames=Fieldnames,delimiter=';')
    for row in reader:
        print(row['Meter Serial Number'], row['Historical Volume'], )
