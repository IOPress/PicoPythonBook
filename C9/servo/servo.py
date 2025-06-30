from machine import Pin, PWM
from time import sleep
class Servo:
    def __init__(self, pinNo):
        self.pwm = PWM(Pin(pinNo))
        self.pwm.freq(50)
        self.position = 65535*2.5/100
    def setPosition(self, p):
        self.position = p
        self.pwm.duty_u16(int(65535*p/1000 + 65535*2.5/100))
servo=Servo(16)
servo.setPosition(100.0)
sleep(1)
servo.setPosition(50.0)
sleep(1)
servo.setPosition(0)
sleep(1)