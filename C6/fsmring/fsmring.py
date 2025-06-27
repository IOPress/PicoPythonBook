from machine import Pin
import time
pinIn = Pin(22, Pin.IN)
pinLED1 = Pin(21, Pin.OUT)
pinLED2 = Pin(20, Pin.OUT)
pinLED3 = Pin(19, Pin.OUT)
pinLED1.on()
pinLED2.off()
pinLED3.off()
s = 0
buttonState = pinIn.value()
while True:
    buttonNow = pinIn.value()
    edge = buttonState-buttonNow
    buttonState = buttonNow
    t = time.ticks_add(time.ticks_us(), 1000*100)
    if s == 0:
        if edge == 1:
            s = 1
            pinLED1.off()
            pinLED2.on()
            pinLED3.off()

    elif s == 1:
        if edge == 1:
            s = 2
            pinLED1.off()
            pinLED2.off()
            pinLED3.on()
    elif s == 2:
        if edge == 1:
            s = 0
            pinLED1.on()
            pinLED2.off()
            pinLED3.off()
    else:
        s = 0
    while time.ticks_us() < t:
        pass
