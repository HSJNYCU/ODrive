# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 21:17:42 2022

@author: forti
"""

from __future__ import print_function

import odrive
from odrive.enums import *
import time
import math

# Find a connected ODrive (this will block until you connect one)
print("finding an odrive...")
my_drive = odrive.find_any()

# Calibrate motor and wait for it to finish
print("starting calibration...")
my_drive.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
while my_drive.axis0.current_state != AXIS_STATE_IDLE:
    time.sleep(0.1)


my_drive.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
time.sleep(1)

# To read a value, simply read the property
print("Bus voltage is " + str(my_drive.vbus_voltage) + "V")
time.sleep(1)

# Or to change a value, just assign to the property
my_drive.axis0.controller.input_pos = 0.5
print("Position setpoint is " + str(my_drive.axis0.controller.pos_setpoint))
time.sleep(1)

# And this is how function calls are done:
for i in [1,2,3,4]:
    print('voltage on GPIO{} is {} Volt'.format(i, my_drive.get_adc_voltage(i)))
time.sleep(1)
