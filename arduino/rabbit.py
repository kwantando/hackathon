#!/usr/bin/env python

# run this ONLY once you have the arduino board connected!!!
# also make sure that you know the device name (thru the Arduino IDE)

import serial
import pika
import time

def sendToRabbitMQ(messageBody): 
	connection = pika.BlockingConnection(pika.ConnectionParameters('54.86.18.251'))
	channel = connection.channel()

	channel.queue_declare(queue='arduino')

	channel.basic_publish(exchange='',
	                      routing_key='arduino',
	                      body=messageBody)
	print " [x] Sent " + messageBody

	channel.close()
	connection.close()

def readFromRabbit():
	connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='54.86.18.251'))
	channel = connection.channel()

	channel.queue_declare(queue='arduino')

	print ' [*] Waiting for messages. To exit press CTRL+C'

	def callback(ch, method, properties, body):
		if(body == "yellow") {
			ser.write(0)
		} else if (body == "blue") {
			ser.write(1)
		} else {
			ser.write(2)
		}
    	print " [x] Received %r" % (body,)

	channel.basic_consume(callback,
				          queue='arduino',
	                      no_ack=True)

	channel.start_consuming()