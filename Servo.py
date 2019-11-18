import smbus			#import SMBus module of I2C
import time
import math

def Drive(kAngleX = 0):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    p = GPIO.PWM(11, 50)
    p.start(0)
    duty = kalAngleX/18.0 + 2.0
    GPIO.output(11, True)
    p.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(11, False)
    p.ChangeDutyCycle(0)
    p.stop()
