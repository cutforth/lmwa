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

InputFile = "20180401_DLC_NoWells.csv"
fileHandle = open(InputFile)
print(fileHandle)
convertFileToDict(fileHandle)
