from machine import Pin
import time
pinIn = Pin(22, Pin.IN)

while True:
    while pinIn.value()==1:
        pass
    while pinIn.value()==0:
        pass

    t=time.ticks_us()
    while pinIn.value()==1:
        pass
    t=time.ticks_diff(time.ticks_us(),t)
    print(t)
    time.sleep(1)
