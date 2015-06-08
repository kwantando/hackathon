#!/usr/bin/env python
import time
import json
import redis
import pika
import datetime
import random

def getCurrentUser():
	users = ['shafeen', 'tyler', 'michael']
	return users[random.randint(0, len(users)-1)]

def getTimestamp():
	return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

def getBuildResult():
	buildResult = ['failure', 'success']
	return buildResult[random.randint(0, len(buildResult)-1)]


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

	time.sleep(2)

	# started build
	statusDict['timestamp'] = getTimestamp()
	statusDict['buildstatus'] = 'inprocess'
	statusDict['buildresult'] = ''
	publishNotification(json.dumps(statusDict))

	time.sleep(1)

	statusDict['timestamp'] = getTimestamp()
	publishNotification(json.dumps(statusDict))

	time.sleep(2)

	# completed build
	statusDict['timestamp'] = getTimestamp()
	statusDict['buildstatus'] = 'complete'
	statusDict['buildresult'] = getBuildResult()
	publishNotification(json.dumps(statusDict))
	
	time.sleep(30)


while 1:
	run()
	



