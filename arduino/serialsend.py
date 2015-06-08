#!/usr/bin/env python
import serial

ser = serial.Serial('/dev/cu.usbserial-DA01HLII', 9600)
while True:
	stringToSend = raw_input("Enter string to send: ")
	ser.write(stringToSend)
