from machine import Pin, PWM,mem32
from time import sleep

class Servo:
    def __init__(self, pinNo):
        self.pwm = PWM(Pin(pinNo))
        self.pin=pinNo
        self.pwm.freq(50)
        self.position = 65535*2.5/100

    def setPosition(self, p):
        self.position = p
        self.pwm.duty_u16(int(65535*p/1000 + 65535*2.5/100))
    
    def getSlice(self):
        return (self.pin>>1) & 0x07
    
    def getChannel(self):
        return self.pin & 1

    def setPolarity(self,invert):
        sliceNo=self.getSlice()
        channel=self.getChannel()
        PWM_BASE=0x400a8000 # 0x40050000 pico
        CH1_CSR=0x14
        Addr = PWM_BASE +CH1_CSR*sliceNo
        if invert:
            mem32[Addr]=mem32[Addr] | 0x1 << (2+channel)
        else:
            mem32[Addr]=mem32[Addr] & ~(0x1<<(2+channel))
servo=Servo(16)

servo.setPosition(100.0)
servo.setPolarity(True)
sleep(1)
servo.setPosition(50.0)
servo.setPolarity(True)
sleep(1)
servo.setPosition(0)
sleep(1)