import threading
import smbus
import math
import types
import ctypes
import time
import subprocess
import pigpio

pi=pigpio.pi()
pi_1=pigpio.pi()
pi_2=pigpio.pi()

pi.write(6, 0) # BCM 将6号引脚设置为低电平
pi.read(6)
pi.set_PWM_frequency(6, 50)#设定6号引脚产生的pwm波形的频率为50Hz
pi.set_PWM_range(6, 2000)



pi_1.write(5, 0) # BCM 将6号引脚设置为低电平。从正面看向陀螺仪，左边的舵机
pi_1.read(5)
pi_1.set_PWM_frequency(5, 50)#设定5号引脚产生的pwm波形的频率为500Hz
pi_1.set_PWM_range(5, 2000)

pi_2.write(13, 0) # BCM 将5号引脚设置为低电平。从正面看向陀螺仪，右边的舵机
pi_2.read(13)
pi_2.set_PWM_frequency(13, 50)#设定13号引脚产生的pwm波形的频率为50Hz
pi_2.set_PWM_range(13, 2000)

#27 right
#22 left
pi_3=pigpio.pi()
pi_3.write(27, 0) # BCM 将27号引脚设置为低电平
pi_3.read(27)
pi_3.set_PWM_frequency(27, 500)#设定27号引脚产生的pwm波形的频率为50Hz
pi_3.set_PWM_range(27, 2000)


pi_4=pigpio.pi()
pi_4.write(22, 0) # BCM 将22号引脚设置为低电平
pi_4.read(22)
pi_4.set_PWM_frequency(22, 500)#设定22号引脚产生的pwm波形的频率为500Hz
pi_4.set_PWM_range(22, 2000)

bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards

addr1= 0x50

addr2 = 0x48

servo_vertical = 140
servo_now_y_ang = 140
servo_now_x_ang=140

y_angle_now = 0
x_angle_now = 0

duty=140

def calc_angle_value(x_angle,y_angle,z_angle):

    x = ((x_angle[1] << 8) | x_angle[0])/32768 * 180

    y = ((y_angle[1] << 8) | y_angle[0])/32768 * 180

    z = ((z_angle[1] << 8) | z_angle[0])/32768 * 180

    if(x >= 180):

        x -= 360

    if(y >= 180):

        y -= 360

    if(z >= 180):

        z -= 360

    return x,y,z

def ReadData(address):

    x_angle = bus.read_i2c_block_data(address,0x3d,2)
   
    y_angle = bus.read_i2c_block_data(address,0x3e,2)
 
    z_angle = bus.read_i2c_block_data(address,0x3f,2)

    x,y,z = calc_angle_value(x_angle,y_angle,z_angle)

    return x,y,z

def Servo_y_angle(n):
    # n is angle,convert it to pwm dutycycle
    DutyCycle = n/0.9
    global servo_now_y_ang
    servo_now_y_ang = servo_vertical + DutyCycle
    if servo_now_y_ang<=100:
        servo_now_y_ang=100
    if servo_now_y_ang>=180:
        servo_now_y_ang=180
    return servo_now_y_ang

def Servo_x_angle(n):
    # n is angle,convert it to pwm dutycycle
    DutyCycle = n*17/18
    global servo_now_x_ang
    servo_now_x_ang = servo_vertical + DutyCycle
    if servo_now_x_ang<=55:
        servo_now_x_ang=55
    if servo_now_x_ang>=225:
        servo_now_x_ang=225
    return servo_now_x_ang

def delayMicrosecond(t):    # 微秒级延时函数
    start,end=0,0           # 声明变量
    start=time.time()       # 记录开始时间
    t=(t-3)/1000000     # 将输入t的单位转换为秒，-3是时间补偿
    while end-start<t:  # 循环至时间差值大于或等于设定值时
        end=time.time()     # 记录结束时间
        end=time.time()     # 记录结束时间
def pi3():
    pi_3.set_PWM_dutycycle(27,1000)
    delayMicrosecond(4000000)
    pi_3.set_PWM_dutycycle(27,1200)
    delayMicrosecond(5000000)
#    time.sleep(5.0)
    pi_3.set_PWM_dutycycle(27,0)

def pi4():
    pi_4.set_PWM_dutycycle(22,1000)
    delayMicrosecond(4000000)
    pi_4.set_PWM_dutycycle(22,1200)
    delayMicrosecond(5000000)
#    time.sleep(5.0)
    pi_4.set_PWM_dutycycle(22,0)

while(True):
    try:
        right_x,right_y,right_z = ReadData(addr1)

        y_angle_now = right_y;
        x_angle_now = right_x;
        
        if abs(servo_now_y_ang - y_angle_now)>=4.5:       
            pi.set_PWM_dutycycle(6,Servo_y_angle(-y_angle_now))
        if abs(servo_now_x_ang - x_angle_now)>=4.5:       
            pi_1.set_PWM_dutycycle(5,Servo_x_angle(x_angle_now))            
            pi_2.set_PWM_dutycycle(13,Servo_x_angle(-x_angle_now))
            
        print("Right Data: {:.4} {:.4} {:.4}".format(right_x,right_y,right_z))
        time.sleep(0.5)           
        
    except ValueError:
        continue

