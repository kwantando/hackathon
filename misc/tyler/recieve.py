#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='54.86.18.251'))
channel = connection.channel()

channel.queue_declare(queue='arduino')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

channel.basic_consume(callback,
                      queue='arduino',
                      no_ack=True)

channel.start_consuming()