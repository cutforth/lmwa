#! /usr/sbin/python

# Craig Cutforth
# LmwaSQLiteMethods.py
# Created: 2018.05.15

import os
import time
import sqlite3
import pdb
import warnings

# Take input from a CSV file.
# For test, keep table structure the same, but create bogus data using bogus CSV file.

BASE_DIR = os.getcwd()

def deleteExistingDB(dbFilename,dbTablename):
    dbConnection = openDB(dbFilename)
    stringCommandStart = 'DROP TABLE IF EXISTS '
    stringCommandFull = stringCommandStart + dbTablename
    dbConnection.cursor().execute('DROP TABLE IF EXISTS ' + dbTablename)
    closeDB(dbConnection)
    os.remove(dbFilename)

def createNewDB(dbFilename):
    dbFilenameString = BASE_DIR + '\\' + dbFilename
    if os.path.exists(dbFilenameString):
        raise ValueError('improper New filename  specified: ',dbFilenameString)
    dbConnection = openDB(dbFilename)
    saveDB(dbConnection)
    closeDB(dbConnection)

def openDB(dbFilename):
    dbConnection = sqlite3.connect(dbFilename)
    return dbConnection

def saveDB(dbConnection):
    dbConnection.commit()

def closeDB(dbConnection):
    dbConnection.close()

def executeSQLCommand(dbConnection, SQLCommand):
    # myDBCursor = dbConnection.cursor()
    # myDBCursor.execute(SQLCommand)
    dbConnection.cursor().execute(SQLCommand)

def createTable(dbConnection, dbTablename, columnNames, columnTypes):
    if len(columnNames) != len(columnTypes):
        warnings.warn('createTable was given name and type vectors of different length')
    tableDescription = '('
    for name,type in zip(columnNames,columnTypes):
        tableDescription = tableDescription + name + ' ' + type + ', '
    tableDescription = tableDescription[0:-2] + ')'
    TABLE_CREATE_COMMAND = 'CREATE TABLE ' + dbTablename + ' ' + tableDescription
    executeSQLCommand(dbConnection,TABLE_CREATE_COMMAND)
    saveDB(dbConnection)

def insertNewRow(dbConnection, dbTablename, columnNames, dataValues):
    SQLCommand = 'INSERT INTO ' + dbTablename + columnNames + ' VALUES ' + dataValues
    # print(SQLCommand)
    dbConnection.cursor().execute(SQLCommand)
    saveDB(dbConnection)
