import time
from time import sleep
from machine import Pin

pin=Pin(22,Pin.IN,Pin.PULL_UP)

event=0
def rise(pin):
    global event
    event=1

def fall(pin):
    global event
    event=2

while True:
    pin.irq(rise, Pin.IRQ_RISING,hard=True)
    while  not(event==1):
        pass
    t=time.ticks_us()
    pin.irq(fall, Pin.IRQ_RISING)
    while  not(event==2):
        pass
    t=time.ticks_diff(time.ticks_us(),t)
    print(t)
    sleep(1)