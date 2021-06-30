import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
pwm = GPIO.PWM(7, 500)
pwm.start(1)
while True:
    pwm.ChangeDutyCycle(55)
    GPIO.output(7, GPIO.HIGH)
    time.sleep(4)
    pwm.stop()
    break