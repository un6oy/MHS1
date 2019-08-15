#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
import sys

MA = ev3.LargeMotor("outA")
MB = ev3.LargeMotor("outB")
MC = ev3.LargeMotor("outC")
MD = ev3.LargeMotor("outD")

CalcPos = [0,0]

def forward(speed = 500,time = 1):
    print('Moving forwards for',time,'at speed',speed)
    MA.run_timed(time_sp = time * 1000, speed_sp=speed) 
    MB.run_timed(time_sp = time * 1000, speed_sp=speed) 
    MC.run_timed(time_sp = time * 1000, speed_sp=speed) 
    MD.run_timed(time_sp = time * 1000, speed_sp=speed) 
    time.sleep(time) 
    CalcPos[0] += 1
def backwards(speed = 500,time = 1):
    print('Moving backwards for',time,'at speed',speed)
    MA.run_timed(time_sp = time * 1000, speed_sp=-speed) 
    MB.run_timed(time_sp = time * 1000, speed_sp=-speed) 
    MC.run_timed(time_sp = time * 1000, speed_sp=-speed) 
    MD.run_timed(time_sp = time * 1000, speed_sp=-speed) 
    time.sleep(time) 
    CalcPos[0] -= 1
def left(speed = 500,time = 1):
    print('Moving left for',time,'at speed',speed)
    MA.run_timed(time_sp = time * 1000, speed_sp=speed) 
    MB.run_timed(time_sp = time * 1000, speed_sp=speed) 
    MC.run_timed(time_sp = time * 1000, speed_sp=-speed) 
    MD.run_timed(time_sp = time * 1000, speed_sp=-speed) 
    time.sleep(time) 
    CalcPos[1] -= 1
def right(speed = 500,time = 1):
    print('Moving right for',time,'at speed',speed)
    MA.run_timed(time_sp = time * 1000, speed_sp=-speed) 
    MB.run_timed(time_sp = time * 1000, speed_sp=-speed) 
    MC.run_timed(time_sp = time * 1000, speed_sp=speed) 
    MD.run_timed(time_sp = time * 1000, speed_sp=speed) 
    time.sleep(time) 
    CalcPos[1] += 1
def diag_forward_left(speed = 500,time = 1):
    forward(time=0.5)
    left(time=0.5)

def diag_forward_right(speed = 500,time = 1):
    forward(time=0.5)
    right(time=0.5)

def diag_backward_left(speed = 500,time = 1):
    backwards(time=0.5)
    left(time=0.5)

def diag_backward_right(speed = 500,time = 1):
    backwards(time=0.5)
    right(time=0.5)

while true:
    forward(time=2)
    diag_forward_left(time=2)
    left(time=2)
    diag_backward_left(time=2)
    backwards(time=2)
    diag_backward_right(time=2)
    right(time=2)
    diag_forward_right(time=2)
    