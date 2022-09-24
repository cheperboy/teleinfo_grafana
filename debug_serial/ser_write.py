#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import the PySerial library and sleep from the time library
import serial
from time import sleep, time

# declare to variables, holding the com port we wish to talk to and the speed
port = '/dev/ttyAMA0'
baud = 9600
lastime = 0
timeout = 10 # 30 seconds timeout

# open a serial connection using the variables above
ser = serial.Serial(port=port, baudrate=baud)
#ser.timeout(1)  # set the read time out to 1 second
# wait for a moment before doing anything else
sleep(0.2)


while True:
    a='hello'.encode('utf-8')
    ser.write(a)
    print("Sent hello")

