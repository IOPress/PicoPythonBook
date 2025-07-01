import rp2
from machine import Pin

@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,rp2.PIO.OUT_LOW),autopull=True)
def output():
    label("again")    
    out(pins,2)
    jmp("again") 

sm = rp2.StateMachine(0, output, freq=2300, out_base=Pin(16), out_shiftdir=rp2.PIO.SHIFT_RIGHT)
sm.active(1)
while True:
    sm.put(0xFEDCBA98)