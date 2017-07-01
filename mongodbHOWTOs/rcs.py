'''
Created on Apr 25, 2017

@author: jackwang
'''
import sys

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import pymongo
import pprint


def main():
    try:
        client = MongoClient(host="localhost", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    db = client["mydb"]
    
    # Assuming we already have a database handle in scope named dbh
    # find a single document with the username "janedoe".
    # find_one() will return None if no document is found
    user_doc = db.users.find_one({"username" : "janedoe"})
    if not user_doc:
        print "no document found for username janedoe"
    
    print "Successfully find one document:"
    pprint.pprint(user_doc, width=1) 

    # Assuming we already have a database handle in scope named dbh
    # find all documents with the firstname "jane".
    # Then iterate through them and print out the email address.
    users = db.users.find({"firstname":"jane"})
    for user in users:
        print user.get("email")

    # Only retrieve the "email" field from each matching document.
    users = db.users.find({"firstname":"jane"}, {"email":1})
    for user in users:
        print user.get("email")

    # Find out how many documents are in users collection, efficiently
    userscount = db.users.find().count()
    print "There are %d documents in users collection" % userscount

    # Return all user with firstname "jane" sorted
    # in descending order by birthdate (ie youngest first)
    users = db.users.find(
        {"firstname":"jane"}).sort(("dateofbirth", pymongo.DESCENDING))
    for user in users:
        print user.get("email")

    # Return all user with firstname "jane" sorted
    # in descending order by birthdate (ie youngest first)
    users = db.users.find({"firstname":"jane"},
    sort=[("dateofbirth", pymongo.DESCENDING)])
    for user in users:
        print user.get("email")

    # Return at most 10 users sorted by score in descending order
    # This may be used as a "top 10 users highscore table"
    users = db.users.find().sort(("score", pymongo.DESCENDING)).limit(10)
    for user in users:
        print user.get("username"), user.get("score", 0)





if __name__ == "__main__":
    main()
    