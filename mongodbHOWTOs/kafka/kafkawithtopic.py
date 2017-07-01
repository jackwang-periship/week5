'''
Created on Apr 27, 2017

@author: jackwang
'''
import sys
import sqlite3

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson.objectid import ObjectId
from kafka import KafkaProducer


def main():

    dboption = ' '.join(sys.argv[1:]) or "No"

    zipcode_doc = {}
    
    if dboption is not "No":
        try:
            client = MongoClient(host="34.201.178.24", port=27017)
        except ConnectionFailure, e:
            sys.stderr.write("Could not connect to MongoDB: %s" % e)
            sys.exit(1)
        db = client["censusdata"]
    
    producer = KafkaProducer(bootstrap_servers='34.201.178.24:9092')

    conn = sqlite3.connect('zipcodeSMALL.db')
    c = conn.cursor()
    for idx, row in enumerate(c.execute("SELECT * FROM ZIPCodes WHERE PrimaryRecord ='P' ORDER BY Population")):
        myresult = ','.join(str(x) for x in row)
        mytopic = row[22]
        producer.send(mytopic, value=myresult),
        if dboption is not "No":
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
    print "Total of %d records were inserted and published." % idx
#     producer.flush()
#     producer.close()

if __name__ == "__main__":
    main()
    