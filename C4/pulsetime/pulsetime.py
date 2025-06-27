from machine import Pin
import time
pin = Pin(22, Pin.OUT)
while True:
    pin.value(1)
    time.sleep_us(10)
    pin.value(0)
    time.sleep_us(10)
