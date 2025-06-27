from machine import Pin
@micropython.native
def flash():
    pin = Pin(22, Pin.OUT)
    while True:
        pin.value(1)
        pin.value(0)
flash()
