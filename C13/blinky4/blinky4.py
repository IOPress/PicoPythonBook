import rp2
from machine import Pin

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW, )
def squarewave():
    pull(block) 
    label("again")
    set(pins, 1)
    mov(x,osr)
    label("loop1")
    jmp(x_dec,"loop1")  
    set(pins, 0)
    mov(x,osr)  
    label("loop2")
    jmp(x_dec,"loop2") 
    jmp("again") 

sm = rp2.StateMachine(0, squarewave, freq=2300, set_base=Pin(16))
sm.active(1)
sm.put(0xFFF)
while(True):
    pass
