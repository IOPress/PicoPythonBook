from machine import Pin
from utime import sleep_us

pin =Pin(22,Pin.IN,Pin.PULL_DOWN) 

while True:
    pin.init(Pin.OUT,Pin.PULL_DOWN,value=1)
    sleep_us(10)
    pin.init(Pin.IN,Pin.PULL_DOWN)
    sleep_us(10)

