#!/usr/bin/env python

import serial
ser = serial.Serial('/dev/cu.usbserial-DA01HLII', 9600)
while True:
	print ser.readline()




