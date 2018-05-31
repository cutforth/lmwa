#! /usr/sbin/python

# Craig Cutforth
# BuildLmwaAccounts.py
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
    TABLE_CREATE_COMMAND = 'CREATE TABLE ' + mytablename + ' ' + tableDescription
    executeSQLCommand(dbConnection,TABLE_CREATE_COMMAND)
    saveDB(dbConnection)

def insertNewRow(dbConnection, dbTablename, columnNames, dataValues):
    SQLCommand = 'INSERT INTO ' + dbTablename + columnNames + ' VALUES ' + dataValues
    # print(SQLCommand)
    dbConnection.cursor().execute(SQLCommand)
    saveDB(dbConnection)

pdb.set_trace()

# Define the filename and table name
myfilename = 'LMWA_ACCOUNTS.db'
mytablename = 'LmwaAccounts'

# Remove the database if it already existed
deleteExistingDB(myfilename,mytablename)

# Create a new database
createNewDB(myfilename)
myDBConnection = openDB(myfilename)

# Setup the database table(s)
# FUTURE IMPROVEMENT: The table name, column names, and types could be read in from a configuration file
myColNames = ('account', 'serial_number', 'address', 'name', 'email', 'username', 'hash')
myColTypes = ('TEXT', 'INTEGER', 'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT')
createTable(myDBConnection, mytablename, myColNames, myColTypes)
# LMWA_ACCOUNTS_TABLE_CREATE_COMMAND = 'CREATE TABLE ' + mytablename + ' (account TEXT, serial_number INTEGER, address TEXT, name TEXT, email TEXT, username TEXT, hash TEXT)'

insertNewRow(myDBConnection, mytablename, '(account, serial_number, address)', '(\'A65656625\', 65656625,\'8637 Hollyhock\')')
insertNewRow(myDBConnection, mytablename, '(account, serial_number, address)', '(\'A65656648\', 65656648,\'8632 Hollyhock\')')
