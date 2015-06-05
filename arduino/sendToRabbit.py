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

