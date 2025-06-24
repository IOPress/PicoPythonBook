from machine import Pin
import time

pin = Pin("LED", Pin.OUT)

while True:
    pin.value(1)
    time.sleep(1)
    pin.value(0)
    time.sleep(1)
