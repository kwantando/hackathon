#!/usr/bin/env python
from constants import host_name
import redis
import pika
import time

r = redis.StrictRedis(host=host_name, port=6379, db=0)



connection = pika.BlockingConnection(pika.ConnectionParameters(host=host_name))
channel = connection.channel()

channel.exchange_declare(exchange='update',
                         type='fanout')


while (1):
	print 'checking for updates'
	time.sleep(5)
	print 'checking complete'



message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='update',
                      routing_key='',
                      body=message)
print " [x] Sent %r" % (message,)
channel.close()
connection.close()


