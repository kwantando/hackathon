#!/usr/bin/env python
from constants import host_name
import redis
import pika
import json

r = redis.StrictRedis(host=host_name, port=6379, db=0)


connection = pika.BlockingConnection(pika.ConnectionParameters(host=host_name))
channel = connection.channel()

channel.exchange_declare(exchange='notify',
                         type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='notify',
                   queue=queue_name)

print '[*] waiting for notification'

def callback(ch, method, properties, body):
	message = json.loads(body)
	r.hset('build','user',(message ['user']))
	r.hset('build','timestamp',(message ['timestamp']))
	r.hset('build','buildstatus',(message ['buildstatus']))
	r.hset('build','buildresult',(message ['buildresult']))

	print 'Receiving:'
	print 'user ' + r.hget('build','user')
	print 'timestamp ' + r.hget('build','timestamp')
	print 'build status ' +  r.hget('build','buildstatus')
	print 'build result ' + r.hget('build','buildresult')
	print



channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()


#starting, inprocess, complete