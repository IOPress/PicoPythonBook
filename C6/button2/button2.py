from machine import Pin
import time
pinIn = Pin(22, Pin.IN,Pin.PULL_UP)
pinLED = Pin("LED", Pin.OUT)

while True:
    while pinIn.value()==1:
        pass
    while pinIn.value()==0:
        pass
    pinLED.on()
    time.sleep(1)
    pinLED.off()
