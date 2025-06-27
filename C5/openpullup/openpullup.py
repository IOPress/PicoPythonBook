from machine import Pin
from utime import sleep_us

pin =Pin(22,Pin.IN,Pin.PULL_UP) 

while True:
    pin.init(Pin.OUT,Pin.PULL_UP,value=0)
    sleep_us(100)
    pin.init(Pin.IN,Pin.PULL_UP)
    sleep_us(100)
