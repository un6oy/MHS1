#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
import sys

MA = ev3.LargeMotor("outA")
MB = ev3.LargeMotor("outB")
MC = ev3.LargeMotor("outC")
MD = ev3.LargeMotor("outD")


def forward(int speed=500,int time=1):
    MA.RUN_TIMED(speed.sp=speed)
    MB.RUN_TIMED(speed.sp=speed)
    MC.RUN_TIMED(speed.sp=speed)
    MD.RUN_TIMED(speed.sp=speed)
def backwards(int speed=500,int time=1):
    MA.RUN_TIMED(speed.sp=-speed)
    MB.RUN_TIMED(speed.sp=-speed)
    MC.RUN_TIMED(speed.sp=-speed)
    MD.RUN_TIMED(speed.sp=-speed)

def left(int speed=500,int time=1):
    MA.RUN_TIMED(speed.sp=speed)
    MB.RUN_TIMED(speed.sp=speed)
    MC.RUN_TIMED(speed.sp=-speed)
    MD.RUN_TIMED(speed.sp=-speed)

def right(int speed=500,int time=1):
    print('Moving right for',time,'at speed',speed)
    MA.RUN_TIMED(speed.sp=-speed)
    MB.RUN_TIMED(speed.sp=-speed)
    MC.RUN_TIMED(speed.sp=speed)
    MD.RUN_TIMED(speed.sp=speed)

def diag_forward_left(int speed=500,int time=1):
    forward(time=0.5)
    left(time=0.5)

def diag_forward_right(int speed=500,int time=1):
    forward(time=0.5)
    right(time=0.5)

def diag_backward_left(int speed=500,int time=1):
    backwards(time=0.5)
    left(time=0.5)

def diag_backward_right(int speed=500,int time=1):
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
    