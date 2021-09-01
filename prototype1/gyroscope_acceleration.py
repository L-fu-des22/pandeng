



#!/usr/bin/python

import smbus

import math

import types

import ctypes

import time

import subprocess

bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards

addr1= 0x50

addr2 = 0x48

def calc_angle_value(x_angle,y_angle,z_angle):

    x = ((x_angle[1] << 8) | x_angle[0])/32768 * 16*9.8

    y = ((y_angle[1] << 8) | y_angle[0])/32768 * 16*9.8

    z = ((z_angle[1] << 8) | z_angle[0])/32768 * 16*9.8

    if(x >= 16*9.8):

        x -= 32*9.8

    if(y >= 16*9.8):

        y -= 32*9.8

    if(z >= 16*9.8):

        z -= 32*9.8

    return x,y,z

def ReadData(address):

    x_angle = bus.read_i2c_block_data(address,0x34,2)
   
    y_angle = bus.read_i2c_block_data(address,0x35,2)
 
    z_angle = bus.read_i2c_block_data(address,0x36,2)

    x,y,z = calc_angle_value(x_angle,y_angle,z_angle)

    return x,y,z

while(True):

    try:

        right_x,right_y,right_z = ReadData(addr1)

#         left_x,left_y,left_z = ReadData(addr2)

        print("Right Data: {:.4} {:.4} {:.4}".format(right_x,right_y,right_z))
        time.sleep(0.1)
#         print("Left Data: {:.4} {:.4} {:.4}".format(left_x,left_y,left_z))
    except ValueError:

        continue
