#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('54.86.18.251'))
channel = connection.channel()

channel.queue_declare(queue='arduino')

body = raw_input('Enter color to blink:')

channel.basic_publish(exchange='',
                      routing_key='arduino',
                      body=body)
print " [x] Sent " + body

channel.close()
connection.close()
