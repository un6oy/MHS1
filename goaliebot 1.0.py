# #!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
import sys
import motortesting as motors
import CStesting as colour
import UStesting as US
button = ev3.Button()
IR = ev3.Sensor("in2", driver_name = "ht-nxt-ir-seek-v2") 
IR.mode = "AC-ALL"
IROut = IR.Value()
IRVal = IR.Strength()

'''
CURRENT PROGRAM MADE FOR CONFIG: 
Compass
IR
Colour
US

Other viable configs are:
2xIR, 2xUS
IR, Compass, 2xUS
'''

def TrackBall():
    # Ball is left
    if IROut(0) < 4:
        motors.left()                             #move left 1cm
        if colour.CheckColourNew() == 1:          #check colour
            motors.backwards(500,2)
        elif colour.CheckColourNew() == 3:
            break    
    elif IROut(0) == 5:
        motors.forward()                          #move forward 1cm
        motors.backwards()                        #move backwards 1cm
        if colour.CheckColourNew() == 1:          #check colour
            motors.backwards(500,2)
        elif colour.CheckColourNew() = 3:
            break    
    elif IROut(0) > 6:
        motors.right()                            #move right 1cm
        if colour.CheckColourNew() == 1:          #check colour
            motors.backwards(500,2)
        elif colour.CheckColourNew() == 3:
            break       
    elif IROut(0) == 0:
        if US.USFCheck = 3:
            motors.left()
            motors.right(500,2)
            motors.left()
        elif US.USFCheck = 1:
            motors.left()
        elif US.USFCheck = 2:
            motors.right()
    else:
        print("IR Error")

while True:
    TrackBall()