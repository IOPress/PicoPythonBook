from machine import  Pin
pin = Pin(22, Pin.OUT)
while True:
    pin.value(1)
    pin.value(0)
