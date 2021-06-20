# #!/usr/bin/python
# import smbus
# import math
# # Power management registers
# power_mgmt_1 = 0x6b
# power_mgmt_2 = 0x6c
# 
# def read_byte(adr):
#     return bus.read_byte_data(address, adr)
# 
# def read_word(adr):
#     high = bus.read_byte_data(address, adr)
#     low = bus.read_byte_data(address, adr+1)
#     val = (high << 8) + low
#     return val
# def read_word_2c(adr):
#     val = read_word(adr)
#     if (val >= 0x8000):
#         return -((65535 - val) + 1)
#     else:
#         return val
# 
# def dist(a,b):
#     return math.sqrt((a*a)+(b*b))
# 
# def get_y_rotation(x,y,z):
#     radians = math.atan2(x, dist(y,z))
#     return -math.degrees(radians)
# 
# def get_x_rotation(x,y,z):
#     radians = math.atan2(y, dist(x,z))
#     return math.degrees(radians)
# 
# bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
# address = 0x50       # This is the address value read via the i2cdetect command
# 
# # Now wake the 6050 up as it starts in sleep mode
# bus.write_byte_data(address, power_mgmt_1, 0)
# 
# print ("gyro data")
# print ("---------")
# 
# gyro_xout = read_word_2c(0x43)
# gyro_yout = read_word_2c(0x45)
# gyro_zout = read_word_2c(0x47)
# 
# print ("gyro_xout: ", gyro_xout, " scaled: ", (gyro_xout / 131))
# print ("gyro_yout: ", gyro_yout, " scaled: ", (gyro_yout / 131))
# print ("gyro_zout: ", gyro_zout, " scaled: ", (gyro_zout / 131))
# 
# print()
# print ("accelerometer data")
# print ("------------------")
# 
# accel_xout = read_word_2c(0x3b)
# accel_yout = read_word_2c(0x3d)
# accel_zout = read_word_2c(0x3f)
# 
# accel_xout_scaled = accel_xout / 16384.0
# accel_yout_scaled = accel_yout / 16384.0
# accel_zout_scaled = accel_zout / 16384.0
# 
# print ("accel_xout: ", accel_xout, " scaled: ", accel_xout_scaled)
# print ("accel_yout: ", accel_yout, " scaled: ", accel_yout_scaled)
# print ("accel_zout: ", accel_zout, " scaled: ", accel_zout_scaled)
# 
# print ("x rotation: " , get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))
# print ("y rotation: " , get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))
# 
# 




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

    x = ((x_angle[1] << 8) | x_angle[0])/32768 * 2000

    y = ((y_angle[1] << 8) | y_angle[0])/32768 * 2000

    z = ((z_angle[1] << 8) | z_angle[0])/32768 * 2000

    if(x >= 2000):

        x -= 4000

    if(y >= 2000):

        y -= 4000

    if(z >= 2000):

        z -= 4000

    return x,y,z

def ReadData(address):

    x_angle = bus.read_i2c_block_data(address,0x37,2)
   
    y_angle = bus.read_i2c_block_data(address,0x38,2)
 
    z_angle = bus.read_i2c_block_data(address,0x39,2)

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
