import time
from machine import Pin
import machine
data = bytearray(b'\xf0\xf1\xf2')

def myHandler(pin):
    global data
    for i in range(3):
        data[i]=0

pin = Pin(22, Pin.IN, Pin.PULL_UP)
pin.irq(myHandler, Pin.IRQ_RISING,hard=True)

while True:
    # pin.irq(None, Pin.IRQ_RISING) # uncomment to disable interrupt
    s=machine.disable_irq()
    for i in range(3):
        data[i] = 255
    if data[0]!=data[1] or data[1]!=data[2] or data[2]!=data[0]:
        print(data) 
    machine.enable_irq(s)
    # pin.irq(myHandler, Pin.IRQ_RISING) # uncomment to disable interrupt
