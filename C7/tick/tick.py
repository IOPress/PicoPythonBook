import time
from machine import Pin
t = 0
def myHandler(pin):
    global t 
   # pin.irq(None, Pin.IRQ_FALLING) #Uncomment to clear interrupts
    temp = time.ticks_us()
    print(time.ticks_diff(temp,t))
    t = temp
    time.sleep(1.5) 
   # pin.irq(myHandler, Pin.IRQ_FALLING) #Uncomment to clear interrupts
    return

pin = Pin(22, Pin.IN, Pin.PULL_UP)
pin.irq(myHandler, Pin.IRQ_FALLING,hard=False)
while(True):
    pass
