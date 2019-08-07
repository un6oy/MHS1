#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
import sys

IR = ev3.Sensor("in2", driver_name = "ht-nxt-ir-seek-v2") 
IR.mode = "AC-ALL"
IROut = IR.Value()
IRVal = IR.Strength()

if 1 <= IROut <= 4:
    pass

#better start working on dis lol or not idk