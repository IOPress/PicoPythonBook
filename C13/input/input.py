import rp2
from machine import Pin
@rp2.asm_pio()
def light():
    label("again") 
    in_(pins,1)   
    push(block)
    jmp("again") 
LED=Pin(17,mode=Pin.OUT)
in1=Pin(16,mode=Pin.IN)
sm = rp2.StateMachine(0, light, freq=2300,in_base=Pin(16))
sm.active(1)
while True:
    flag = sm.get()
    if (flag == 0):
        LED.value(0)
    else:
        LED.value(1)