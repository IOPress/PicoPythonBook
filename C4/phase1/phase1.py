from machine import Pin
pin1 = Pin(21, Pin.OUT)
pin2 = Pin(22, Pin.OUT)
while True:
    pin1.value(1)
    pin2.value(0)
    pin1.value(0)
    pin2.value(1)
