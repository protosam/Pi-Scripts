#!/usr/bin/env python3

# Reference script for ADXL335 (Adafruit Accelerometer)
# For Raspberry Pi
# https://www.adafruit.com/product/163

# Configure which pins are XYZ axis.
# Refer to BCM pin numbers from https://pinout.io
PIN_Z = 17 # PI pin 11
PIN_Y = 18 # PI pin 12
PIN_X = 27 # PI pin 13

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_Z, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_Y, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_X, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


last_axis_z = 0.0
last_axis_y = 0.0
last_axis_x = 0.0

while True:
    axis_z = GPIO.input(PIN_Z)
    axis_y = GPIO.input(PIN_X)
    axis_x = GPIO.input(PIN_Y)

    if axis_z != last_axis_z or axis_y != last_axis_y or axis_x != last_axis_x:
        print("Z=" + str(axis_z) + ", Y=" + str(axis_y) + ", X=" + str(axis_x))
        last_axis_z = axis_z
        last_axis_y = axis_y
        last_axis_x = axis_x
