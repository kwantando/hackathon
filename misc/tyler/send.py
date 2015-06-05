#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('54.86.18.251'))
channel = connection.channel()

channel.queue_declare(queue='hello2')

channel.basic_publish(exchange='',
                      routing_key='hello2',
                      body='Hello World!!!!!!')
print " [x] Sent 'Hello World!'"

channel.close()
connection.close()
