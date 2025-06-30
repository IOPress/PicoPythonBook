from utime import sleep_ms
from machine import Pin
import machine

class StepperBi4():
    def __init__(self, pinA):
        self.phase=0
        self.pinA=pinA
        self.timer=None
        self.forward=True
        self.speed=0

        self.gpios= tuple([Pin(pinA,Pin.OUT),Pin(pinA+1,Pin.OUT),
                           Pin(pinA+2,Pin.OUT),Pin(pinA+3,Pin.OUT)])
        self.gpios[0].high()
        self.gpioMask=0xF<<self.pinA
        self.halfstepSeq =[0x1, 0x3, 0x2, 0x6, 0x4, 0xC, 0x8, 0x9]
#   [
#             [0,0,0,1],            
#             [0,0,1,1],          
#             [0,0,1,0],
#             [0,1,1,0],
#             [0,1,0,0],        
#             [1,1,0,0],      
#             [1,0,0,0],      
#             [1,0,0,1]
#    ]      

    def _gpio_set(self,value,mask): 
   		# 0x01C for Pico 0x028 for Pico 2
        machine.mem32[0xd0000000+0x028]= (machine.mem32[0xd0000000+0x010])^value & mask

    def setPhase(self,phase):
        value=self.halfstepSeq[phase] << self.pinA
        self._gpio_set(value,self.gpioMask)
        self.phase=phase

    def stepForward(self):
        self.phase=(self.phase+1) % 8        
        self.setPhase(self.phase)
        
    def stepReverse(self):
        self.phase=(self.phase-1) % 8
        self.setPhase(self.phase)
    
    def doRotate(self,timer):
        if self.forward:
            self.stepForward()
        else:
            self.stepReverse()

    def rotate(self,forward,speed):
        self.forward=forward
        self.speed=speed
        if speed==0:
            self.timer.deinit()
            self.timer=None
            return
        if self.timer==None:
            self.timer=machine.Timer()
        self.timer.init(freq=speed,mode=
             machine.Timer.PERIODIC,callback=self.doRotate)


step=StepperBi4(16)
step.setPhase(0)
while True:
    step.rotate(True,100)
    sleep_ms(500)
    step.rotate(True,0)
    sleep_ms(500)

