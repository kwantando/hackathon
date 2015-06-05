import serial
import pika
import time
from sendToRabbit import sendToRabbitMQ

serialDeviceName = '/dev/cu.usbserial-DA01HLII' # CHANGE THIS!!!

ser = serial.Serial(serialDeviceName, 9600)
#dataToWrite = "some string to write"
#ser.write(dataToWrite)

time.sleep(2)

while True:
	arduino_input = ser.readline()
	sendToRabbitMQ("arduino input: " + arduino_input)
	print "arduino input: " + arduino_input

