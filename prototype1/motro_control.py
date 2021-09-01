import threading
import pigpio
import time

#27 right
#22 left
pi_3=pigpio.pi()
pi_3.write(27, 0) # BCM 将4号引脚设置为低电平
pi_3.read(27)
pi_3.set_PWM_frequency(27, 500)#设定14号引脚产生的pwm波形的频率为50Hz
pi_3.set_PWM_range(27, 2000)


pi_4=pigpio.pi()
pi_4.write(22, 0) # BCM 将4号引脚设置为低电平
pi_4.read(22)
pi_4.set_PWM_frequency(22, 500)#设定14号引脚产生的pwm波形的频率为50Hz
pi_4.set_PWM_range(22, 2000)

def delayMicrosecond(t):    # 微秒级延时函数
    start,end=0,0           # 声明变量
    start=time.time()       # 记录开始时间
    t=(t-3)/1000000     # 将输入t的单位转换为秒，-3是时间补偿
    while end-start<t:  # 循环至时间差值大于或等于设定值时
        end=time.time()     # 记录结束时间
def pi3():
    pi_3.set_PWM_dutycycle(27,1300)
    delayMicrosecond(5000000)
#    time.sleep(5.0)
    pi_3.set_PWM_dutycycle(27,0)

def pi4():
    pi_4.set_PWM_dutycycle(22,1300)
    delayMicrosecond(5000000)
#    time.sleep(5.0)
    pi_4.set_PWM_dutycycle(22,0)

if __name__ == '__main__':
    t1 = threading.Thread(target=pi3, args=())
    t2 = threading.Thread(target=pi4, args=())
    t1.start()
    t2.start()




