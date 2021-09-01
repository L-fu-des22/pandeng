# -*- coding: utf-8 -*-
#!/usr/bin/env python    

import pigpio
import time
pi=pigpio.pi()
pi.write(6, 0) # BCM 将4号引脚设置为低电平
pi.read(6)
pi.set_PWM_frequency(6, 50)#设定14号引脚产生的pwm波形的频率为50Hz
pi.set_PWM_range(6, 2000)
#指定要把14号引脚上的一个pwm周期分成多少份，这里是分成2000份，这个数据的范围是25-40000        
#The range of pwm is (50,250),One serving corresponds to 0.9°
#It is recommended to adjust every two copies
#range:95(CCW)~140(vertical)~185(CW) 
pi.set_PWM_dutycycle(6,140)
time.sleep(0.5)
#指定pwm波形的占空比，这里的占空比为150/2000,2000是上一个函数设定的



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
