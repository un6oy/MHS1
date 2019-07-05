#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
import sys

Compass = ev3.Sensor("in3", driver_name = "ht-nxt-compass")
Compass.mode = "COMPASS"

#225 is south