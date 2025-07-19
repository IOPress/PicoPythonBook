from machine import Pin
import time
pinIn = Pin(22, Pin.IN,Pin.PULL_UP)
pinLED = Pin("LED", Pin.OUT)

while True:
    while pinIn.value()==1:
        pass
    t=time.ticks_ms()
    time.sleep_ms(1)
    while pinIn.value()==0:
        pass
    t=time.ticks_diff(time.ticks_ms(),t)
    if t<2000:
        pinLED.on()
        time.sleep(1)
        pinLED.off()
    else:
        for i in range(10):
            pinLED.on()
            time.sleep_ms(100)
            pinLED.off()
            time.sleep_ms(100)
