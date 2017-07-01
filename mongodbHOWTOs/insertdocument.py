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

from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


user_doc = {
    "username" : "janedoe",
    "firstname" : "Jane",
    "surname" : "Doe",
    "dateofbirth" : datetime(1974, 4, 12),
    "email" : "janedoe74@example.com",
    "score" : 0
}

def main():
    try:
        client = MongoClient(host="localhost", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    db = client["mydb"]
    
    db.Users.insert(user_doc)
    print "Successfully inserted document: %s" % user_doc


if __name__ == "__main__":
    main()