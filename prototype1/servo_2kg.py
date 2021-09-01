# -*- coding: utf-8 -*-
#!/usr/bin/env python    

import pigpio
import time

duty=140

pi_1=pigpio.pi()
pi_2=pigpio.pi()

pi_1.write(5, 0) # BCM 将5号引脚设置为低电平 left
pi_2.write(13, 0) # BCM 将5号引脚设置为低电平 right

pi_1.read(5)
pi_2.read(13)

pi_1.set_PWM_frequency(5, 50)#设定18号引脚产生的pwm波形的频率为500Hz
pi_1.set_PWM_range(5, 2000)
pi_2.set_PWM_frequency(13, 50)#设定18号引脚产生的pwm波形的频率为500Hz
pi_2.set_PWM_range(13, 2000)

#指定要把18号引脚上的一个pwm周期分成多少份，这里是分成2000份，这个数据的范围是25-40000        

#20kg:50~250
#2kg:55~225
pi_1.set_PWM_dutycycle(5,duty) #less than 140, CW,left
pi_2.set_PWM_dutycycle(13,duty)

time.sleep(0.5)
#指定pwm波形的占空比，这里的占空比为1500/2000,2000是上一个函数设定的



# import RPi.GPIO as GPIO  
# import time     
# GPIO.setwarnings(False)
# servopin = 12  
# GPIO.setmode(GPIO.BOARD)  
# GPIO.setup(servopin, GPIO.OUT)
# p = GPIO.PWM(servopin,50) #50HZ  
# p.start(0)   
# p.ChangeDutyCycle(7)
# time.sleep(0.5)#归零信号   
# p.stop()  

