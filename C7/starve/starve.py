import time
from machine import Pin

def myHandler(pin):
    print("IRQ") 

pin = Pin(22, Pin.IN, Pin.PULL_UP)
pin.irq(myHandler, Pin.IRQ_RISING, hard=False)
while True:
    print()
    print("doing something useful")
