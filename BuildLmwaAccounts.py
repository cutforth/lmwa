#! /usr/sbin/python

# Craig Cutforth
# BuildLmwaAccounts.py
# Created: 2018.05.15

import os
import time
import sqlite3

# Take input from a CSV file.
# For test, keep table structure the same, but create bogus data using bogus CSV file.

BASE_DIR = os.getcwd()

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
    myDBCursor = dbConnection.cursor()
    myDBCursor.execute(SQLCommand)

myfilename = 'LMWA_ACCOUNTS.db'
createNewDB(myfilename)
print(myfilename,' did not exist!')
myDBConnection = openDB(myfilename)
LMWA_ACCOUNTS_TABLE_CREATE_COMMAND = 'CREATE TABLE LmwaAccounts (account TEXT, serial_number INTEGER, address TEXT, name TEXT, email TEXT, username TEXT, hash TEXT)'
executeSQLCommand(myDBConnection,LMWA_ACCOUNTS_TABLE_CREATE_COMMAND)
saveDB(myDBConnection)

# INSERT_CUTFORTH = 'INSERT INTO LmwaAccounts (account, serial_number, address, name, email, username, hash) VALUES ('A65656625', 65656625,'8637 Hollyhock', 'Craig Cutforth', 'craig.cutforth@gmail.com', 'cutforth', 'TBD')'
INSERT_CUTFORTH = "INSERT INTO LmwaAccounts (account, serial_number, address) VALUES (?, ?, ?)',('A65656625', 65656625,'8637 Hollyhock')"
executeSQLCommand(myDBConnection,INSERT_CUTFORTH)
saveDB(myDBConnection)
