#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
import sys

CS = ev3.ColorSensor("in1")
CS.mode = "COL-COLOR"