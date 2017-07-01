'''
Created on Apr 24, 2017

@author: jackwang
'''
from pymongo import MongoClient
from pymongo import errors
import datetime

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
    }

try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['test-database']
    posts = db['posts']
    record_id = posts.insert(post)
    
except errors as err:
    print str(err)

client.close()    
print record_id
