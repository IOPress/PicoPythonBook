from machine import Pin
import time
pin = Pin(22, Pin.OUT)
n = 10
while True:
    for i in range(n):
        pass
    pin.value(1)
    for i in range(n):
        pass
    pin.value(0)
