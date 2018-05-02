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

Fieldnames = ['Meter Serial Number','Meter Time','Consumption Type',,,,,,,,,'Volume','Volume Units','Operating Time','Operating Time Units']

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
    reader = csv.DictReader(CsvFileHandle,fieldnames=['A','B'],delimiter=';')
    for row in reader:
        print(row['A'], row['B'])
