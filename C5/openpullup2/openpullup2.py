from machine import Pin
from utime import sleep_us

pin =Pin(22,Pin.OPEN_DRAIN,Pin.PULL_UP) 

while True:
    pin.low()
    sleep_us(100)
    pin.high()
    sleep_us(100)
