'''
Created on May 1, 2017

@author: student
'''
import sys
from kafka import KafkaConsumer


atopic = ' '.join(sys.argv[1:]) or "NJ"

consumer = KafkaConsumer(bootstrap_servers='34.201.178.24:9092',
                                 auto_offset_reset='earliest')
consumer.subscribe([atopic])
for message in consumer:
    print (message)

print "Done!"
