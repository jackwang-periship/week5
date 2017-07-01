'''
Created on Apr 25, 2017

@author: jackwang
'''
import sys

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import pprint
import copy


def main():
    
    try:
        client = MongoClient(host="localhost", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    db = client["mydb"]
    
    old_user_doc = db.users.find_one({"username":"janedoe"})
    new_user_doc = copy.deepcopy(old_user_doc)
    # modify the copy to change the email address
    new_user_doc["email"] = "janedoe74@example2.com"
    # run the update query
    # replace the matched document with the contents of new_user_doc
    db.users.update({"username":"janedoe"}, new_user_doc)



if __name__ == "__main__":
    main()
  