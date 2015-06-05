#!/usr/bin/env python
import time
import json
import redis
import pika
import datetime


def getCurrentUser():
	return "defaultUser"

def getTimestamp():
	return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

def getBuildResult():
	return 'failure'


def publishNotification(jsonNotificationData):
	hostaddr = '54.86.18.251'
	connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostaddr))
	channel = connection.channel()
	channel.exchange_declare(exchange='notify', type='fanout')

	message = jsonNotificationData
	channel.basic_publish(exchange='notify',
	                      routing_key='',
	                      body=message)
	
	print " [x] Sent %r to %s" % (message, hostaddr)
	channel.close()
	connection.close()



def run():
	statusDict = {'user' : getCurrentUser()}

	# starting build
	statusDict['timestamp'] = getTimestamp()
	statusDict['buildstatus'] = 'starting'
	statusDict['buildresult'] = ''
	publishNotification(json.dumps(statusDict))

	time.sleep(1)

	# started build
	statusDict['timestamp'] = getTimestamp()
	statusDict['buildstatus'] = 'inprocess'
	statusDict['buildresult'] = ''
	publishNotification(json.dumps(statusDict))

	time.sleep(1)

	# completed build
	statusDict['timestamp'] = getTimestamp()
	statusDict['buildstatus'] = 'complete'
	statusDict['buildresult'] = getBuildResult()
	publishNotification(json.dumps(statusDict))



while 1:
	run()




