#!/bin/python
# Written by Michael Bauer, from examples found around the interwebs.

############################
######### Includes #########
############################

from __future__ import division
import time

import Adafruit_PCA9685

############################
##### Global Variables #####
############################
# Servo Mappings
# Front Right Servos: 1A/1B Channel: 0/4
channel_FR1A = 0
channel_FR1B = 4
# Rear Right Servos: 2A/2B  Channel: 1/5
channel_RR2A = 1
channel_RR2B = 5
# Rear Left Servos: 3A/3B   Channel: 2/6
channel_RL3A = 2
channel_RL3B = 6
# Front Left Servos: 4A/4B  Channel: 3/7
channel_FL4A = 0
channel_FL4B = 4

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)
############################

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Helper function to take one full step forward.
def one_step_forward():
    pwm.set_pwm(channel_FR1B, 0, servo_max)
    pwm.set_pwm(channel_RL3B, 0, servo_max)
    pwm.set_pwm(channel_FR1A, 0, servo_max)
    pwm.set_pwm(channel_RL3A, 0, servo_max)
    time.sleep(1)
    pwm.set_pwm(channel_FR1B, 0, servo_min)
    pwm.set_pwm(channel_RL3B, 0, servo_min)
    pwm.set_pwm(channel_FR1A, 0, servo_min)
    pwm.set_pwm(channel_RL3A, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(channel_FL4B, 0, servo_max)
    pwm.set_pwm(channel_RR2B, 0, servo_max)
    pwm.set_pwm(channel_FL4A, 0, servo_max)
    pwm.set_pwm(channel_RR2A, 0, servo_max)
    time.sleep(1)
    pwm.set_pwm(channel_FL4B, 0, servo_min)
    pwm.set_pwm(channel_RR2B, 0, servo_min)
    pwm.set_pwm(channel_FL4A, 0, servo_min)
    pwm.set_pwm(channel_RR2A, 0, servo_min)
    time.sleep(1)
    
print('Walking, press Ctrl-C to quit...')
while True:
    one_step_forward():
    
