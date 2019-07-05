#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
import sys

IR = ev3.Sensor("in2", driver_name = "ht-nxt-ir-seek-v2") 
IR.mode = "AC-ALL"