import rp2
from machine import Pin

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink():
    label("again") 
    wait(0,pin, 0)   
    wait(1,pin, 0)
    set(pins, 1)
    set(pins, 0)
    jmp("again") 

in1=Pin(16,mode=Pin.IN)
sm = rp2.StateMachine(0, blink,  
               freq=2300,in_base=Pin(16),set_base=Pin(17))
sm.active(1)
while(True):
    pass