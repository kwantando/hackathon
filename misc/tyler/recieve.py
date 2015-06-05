#!/usr/bin/env python
import pika
import serial
import time
import json 

connection = pika.BlockingConnection(pika.ConnectionParameters(
host='54.86.18.251'))
channel = connection.channel()

channel.exchange_declare(exchange='clientupdate', type='fanout')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='clientupdate', queue=queue_name)

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
	
	body = json.loads(body)

	serialDeviceName = '/dev/cu.usbserial-DA01HLII' # CHANGE THIS!!!
	ser = serial.Serial(serialDeviceName, 9600)


	if(body['buildstatus'] == "starting"):
		ser.write('0')
	elif(body['buildstatus'] == "inprocess"):
		ser.write('1')
	else:
		ser.write('2')
	print " [x] Received %r" % (body,)

channel.basic_consume(callback,
			          queue=queue_name,
                      no_ack=True)

channel.start_consuming()