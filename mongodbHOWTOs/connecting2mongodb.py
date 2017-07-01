'''
Created on Apr 25, 2017

@author: jackwang
'''
""" An example of how to connect to MongoDB """
import sys

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def main():
    """ Connect to MongoDB """
    try:
        c = MongoClient(host="localhost", port=27017)
        print "Connected successfully"
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)

if __name__ == "__main__":
    main()
