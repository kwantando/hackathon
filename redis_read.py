#!/usr/bin/env python
from constants import host_name
import redis
import pika
import time
import json

r = redis.StrictRedis(host=host_name, port=6379, db=0)

connection = pika.BlockingConnection(pika.ConnectionParameters(host=host_name))
channel = connection.channel()

channel.exchange_declare(exchange='clientupdate',
                         type='fanout')

saved_timestamp = 'nodata'

while (1):
	current_timestamp = r.hget("build","timestamp")
	if (saved_timestamp != current_timestamp):
		saved_timestamp = current_timestamp 

		data = {}
		data['buildstatus'] = r.hget("build","buildstatus")
		message = json.dumps(data)
		channel.basic_publish(exchange='clientupdate',
                      routing_key='',
                      body=message)
		print ' [*] sending ' + message
 	time.sleep(1)
 


channel.close()
connection.close()


