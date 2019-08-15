#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
import sys


CS = ev3.ColorSensor("in1")
CS.mode = "COL-COLOR"
def CheckColourNew():

    CSOut = CS.value()

    print(CSOut)
    if CSOut == 1:
        print("Black")
        return 1
    elif CSOut == 3:
        print("Green")
        return 2
    else:
        print("Other Colour")
        return 3

while True:
    colour = CheckColourNew()
    print(colour)
    time.sleep(1)