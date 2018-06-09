#! /usr/sbin/python

# Craig Cutforth
# BuildLmwaAccounts.py
# Created: 2018.05.15

import os
import time
# import sqlite3
import pdb
# pdb.set_trace()
import warnings
import LmwaSQLiteMethods as SQL

# Take input from a CSV file.
# For test, keep table structure the same, but create bogus data using bogus CSV file.

# Define the filename and table name
myfilename = 'LMWA_ACCOUNTS.db'
mytablename = 'LmwaAccounts'

# Remove the database if it already existed
SQL.deleteExistingDB(myfilename,mytablename)

# Create a new database
SQL.createNewDB(myfilename)
myDBConnection = SQL.openDB(myfilename)

# Setup the database table(s)
# FUTURE IMPROVEMENT: The table name, column names, and types could be read in from a configuration file
myColNames = ('account', 'serial_number', 'address', 'name', 'email', 'username', 'hash')
myColTypes = ('TEXT', 'INTEGER', 'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT')
SQL.createTable(myDBConnection, mytablename, myColNames, myColTypes)
# LMWA_ACCOUNTS_TABLE_CREATE_COMMAND = 'CREATE TABLE ' + mytablename + ' (account TEXT, serial_number INTEGER, address TEXT, name TEXT, email TEXT, username TEXT, hash TEXT)'

SQL.insertNewRow(myDBConnection, mytablename, '(account, serial_number, address)', '(\'A65656625\', 65656625,\'8637 Hollyhock\')')
SQL.insertNewRow(myDBConnection, mytablename, '(account, serial_number, address)', '(\'A65656648\', 65656648,\'8632 Hollyhock\')')
