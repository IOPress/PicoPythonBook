import rp2
from machine import Pin

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW, )
def blink():
    label("again")
    set(pins, 1)
    set(x,31)
    label("loop1")
    nop() [31]
    jmp(x_dec,"loop1")  
    set(pins, 0)  
    set(x,31)
    label("loop2")
    nop() [31]
    jmp(x_dec,"loop2") 
    jmp("again")  

sm = rp2.StateMachine(0, blink, freq=2300, set_base=Pin(16))
sm.active(1)
while(True):
    pass
