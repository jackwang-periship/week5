'''
Created on Apr 25, 2017

@author: jackwang
'''
""" 
An example of how to use MongoDB Replica Set

* MongoClient which does acknowledged writes by default

A connection to a replica set can be made using the MongoClient() constructor, 
specifying one or more members of the set, along with the replica set name. 
Any of the following connects to the replica set we just created:

The addresses passed to MongoClient() are called the seeds. 
As long as at least one of the seeds is online, 
MongoClient discovers all the members in the replica set, 
and determines which is the current primary and which are secondaries or arbiters. 
Each seed must be the address of a single mongod. Multihomed and round robin DNS addresses are not supported.

The MongoClient constructor is non-blocking: the constructor returns immediately 
while the client connects to the replica set using background threads. 
Note how, if you create a client and immediately print the string representation of its nodes 
attribute, the list may be empty initially. If you wait a moment, 
MongoClient discovers the whole replica set:


"""
import sys
import sqlite3

from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, AutoReconnect, NotMasterError
from bson.objectid import ObjectId


def main():

    zipcode_doc = {}
    
    try:
    #The addresses passed to MongoClient() are called the seeds. 
    #As long as at least one of the seeds is online, 
    #MongoClient discovers all the members in the replica set, 
    #and determines which is the current primary and which are secondaries or arbiters. 
    #Each seed must be the address of a single mongod. Multihomed and round robin DNS addresses are not supported.
        client = MongoClient(host="mongodb://mongo-admin:password@mongo-repl-1:27017, mongo-repl-2:27017, mongo-repl-3:27017/?replicaSet=rs0")
        db = client["censusdata"]
    
        conn = sqlite3.connect('mongodb\zipcodeSMALL.db')
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for idx, row in enumerate(c.execute("SELECT * FROM ZIPCodes WHERE PrimaryRecord ='P'")):
            zipcode_doc['ZipCode'] = row[0]
            zipcode_doc['Latitude'] = row[19]
            zipcode_doc['Longitude'] = row[20]
            zipcode_doc['State'] = row[22]
            zipcode_doc['AreaCode'] = row[26]
            zipcode_doc['City'] = row[27]
            zipcode_doc['TimeZone'] = row[32]
            zipcode_doc['Population'] = row[2]
            zipcode_doc['WhitePopulation'] = row[4]
            zipcode_doc['BlackPopulation'] = row[5]
            zipcode_doc['HispanicPopulation'] = row[6]
            zipcode_doc['AsianPopulation'] = row[7]
            zipcode_doc['HawaiianPopulation'] = row[8]
            zipcode_doc['IndianPopulation'] = row[9]
            zipcode_doc['OtherPopulation'] = row[10]
            zipcode_doc['_id'] = ObjectId() 
            db.ZIPCodes.insert(zipcode_doc)
            print "Successfully inserted document: %s" % zipcode_doc
        print "Total of %d records were inerted." % idx
    except AutoReconnect, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    except NotMasterError, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    

if __name__ == "__main__":
    main()