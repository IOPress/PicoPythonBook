from machine import Pin, PWM
from time import sleep
class Motor:
    def __init__(self, pinNo):
        self.gpio = pinNo
        self._on = False
        self.speed=0
        self.pwm1=PWM(Pin(pinNo))
        self.pwm1.freq(2000)
        self.pwm1.duty_u16(0)
    def setSpeed(self,s):
        self._on=True
        self.speed=s
        self.pwm1.duty_u16(int(65535*s/100))    
    def off(self):
        self._on=False
        self.pwm1.duty_u16(0)    
    def on(self):
        self._on=True
        self.pwm1.duty_u16(int(65535*self.speed/100))
motor=Motor(16)
motor.setSpeed(50)
sleep(1)
motor.off()
sleep(1)
motor.setSpeed(90)
sleep(1)
motor.off()
