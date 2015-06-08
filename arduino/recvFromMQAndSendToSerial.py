#!/usr/bin/env python
import pika
import serial
import time
import json 

serialDeviceName = '/dev/cu.usbserial-DA01HLII' # CHANGE THIS!!!
ser = serial.Serial(serialDeviceName, 9600)

connection = pika.BlockingConnection(pika.ConnectionParameters(
host='54.86.18.251'))
channel = connection.channel()

channel.exchange_declare(exchange='clientupdate', type='fanout')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='clientupdate', queue=queue_name)

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
	print " [x] Received %r" % (body,)
	body = json.loads(body)
	
	if(body['buildstatus'] == 'starting'):
		print "sending 'starting' to serial"
		ser.write('starting')
	elif(body['buildstatus'] == 'inprocess'):
		print "sending 'inprocess' to serial"
		ser.write('inprocess')
	else:
		print "sending 'complete' to serial"
		ser.write('complete')
	print " [x] Received %r" % (body,)

channel.basic_consume(callback,
			          queue=queue_name,
                      no_ack=True)

channel.start_consuming()