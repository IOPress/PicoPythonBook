from machine import Pin
import time

pin = Pin(22,Pin.OUT)
while True:
    pin.toggle()
    time.sleep(1)
