import rp2
from machine import Pin

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW)
def squarewave():
    label("again")    
    nop().side(1)
    jmp("again").side(0) 

sm = rp2.StateMachine(0, squarewave, freq=2300,sideset_base=Pin(16))
sm.active(1)
while(True):
    pass
