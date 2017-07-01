'''
Created on Apr 25, 2017

@author: jackwang
'''
""" 
An example of how to insert a document

* MongoClient which does acknowledged writes by default

* Be aware: MongoDB inserts will generate the primary key automatically. In
MongoDB, the _id property on a document is treated specially. It is considered to be
the primary key for that document, and is expected to be unique unless the collection
has been explcitly created without an index on _id .

* By default, the PyMongo driver performs asynchronous writes. Write operations in-
clude insert, update, remove and findAndModify.


 
"""
import sys
import sqlite3

from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson.objectid import ObjectId


def main():

    zipcode_doc = {}
    
    try:
        client = MongoClient(host="localhost", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    db = client["censusdata"]

    conn = sqlite3.connect('zipcodeSMALL.db')
    c = conn.cursor()
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

if __name__ == "__main__":
    main()