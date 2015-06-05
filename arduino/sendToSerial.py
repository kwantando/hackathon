#!/usr/bin/env python

# run this ONLY once you have the arduino board connected!!!
# also make sure that you know the device name (thru the Arduino IDE) 

import serial

serialDeviceName = '/dev/tty.usbserial' # CHANGE THIS!!!

ser = serial.Serial(serialDeviceName, 9600)
dataToWrite = "some string to write"
ser.write(dataToWrite)
