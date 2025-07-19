from machine import Pin
import time
pinIn = Pin(22, Pin.IN,Pin.PULL_UP)
pinLED = Pin("LED", Pin.OUT)

while True:
    if pinIn.value():
        pinLED.on()
    else:
        pinLED.off()
    time.sleep(0.5)
