#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
import sys

Compass = ev3.Sensor("in4", driver_name = "ht-nxt-compass")
Compass.mode = "COMPASS"

while True:
    CVal = Compass.value(0)
    print(CVal)