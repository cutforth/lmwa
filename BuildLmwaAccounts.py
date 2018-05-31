#! /usr/sbin/python

# Craig Cutforth
# BuildLmwaAccounts.py
# Created: 2018.05.15

import os
import time
import sqlite3
import pdb

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

def insertNewRow(dbConnection, dbTablename, columnNames, dataValues):
    SQLCommand = 'INSERT INTO ' + dbTablename + columnNames + ' VALUES ' + dataValues
    print(SQLCommand)
    dbConnection.cursor().execute(SQLCommand)
    saveDB(dbConnection)

pdb.set_trace()

myfilename = 'LMWA_ACCOUNTS.db'
mytablename = 'LmwaAccounts'

# Remove the database if it already existed
deleteExistingDB(myfilename,mytablename)

# Create a new database
createNewDB(myfilename)
# print(myfilename,' did not exist!')
myDBConnection = openDB(myfilename)

# Setup the database table(s)
# FUTURE IMPROVEMENT: The table name, column names, and types could be read in from a configuration file
LMWA_ACCOUNTS_TABLE_CREATE_COMMAND = 'CREATE TABLE ' + mytablename + ' (account TEXT, serial_number INTEGER, address TEXT, name TEXT, email TEXT, username TEXT, hash TEXT)'
executeSQLCommand(myDBConnection,LMWA_ACCOUNTS_TABLE_CREATE_COMMAND)
saveDB(myDBConnection)

# INSERT_CUTFORTH = 'INSERT INTO LmwaAccounts (account, serial_number, address, name, email, username, hash) VALUES ('A65656625', 65656625,'8637 Hollyhock', 'Craig Cutforth', 'craig.cutforth@gmail.com', 'cutforth', 'TBD')'
# INSERT_CUTFORTH = "'INSERT INTO LmwaAccounts (account, serial_number, address) VALUES (?, ?, ?)',('A65656625', 65656625,'8637 Hollyhock')"
# executeSQLCommand(myDBConnection,INSERT_CUTFORTH)

# myDBConnection.cursor().execute('INSERT INTO LmwaAccounts (account, serial_number, address) VALUES (?, ?, ?)',('A65656625', 65656625,'8637 Hollyhock'))
insertNewRow(myDBConnection, mytablename, '(account, serial_number, address)', '(\'A65656625\', 65656625,\'8637 Hollyhock\')')
insertNewRow(myDBConnection, mytablename, '(account, serial_number, address)', '(\'A65656648\', 65656648,\'8632 Hollyhock\')')

# LMWA_ACCOUNTS_ADD_HARRIS_INFO = '(\'A65656648\', 65656648, \'8632 Hollyhock\')'
# INSERT_HARRIS = 'INSERT INTO ' + mytablename + ' (account, serial_number, address) VALUES (?, ?, ?)\', ' + LMWA_ACCOUNTS_ADD_HARRIS_INFO
# pdb.set_trace()
# executeSQLCommand(myDBConnection,INSERT_HARRIS)
# myDBConnection.cursor().execute('INSERT INTO LmwaAccounts (account, serial_number, address) VALUES (?, ?, ?)',('A65656648', 65656648,'8632 Hollyhock'))
# saveDB(myDBConnection)

# executeSQLCommand(myDBConnection)
