from machine import Pin
import time
pinIn = Pin(22, Pin.IN)

s=0
while True:
    i=pinIn.value()
    t=time.ticks_add(time.ticks_us(),1000*100)
    if s==0:       #button not pushed
        if i:
            s=1
        tpush=t
    elif s==1:     #button pushed
        if not i:
            s=0
            if time.ticks_diff(t, tpush) > 2000000:
                print("Button held \n\r")                
            else:
                print("Button pushed \n\r")
    else:
        s=0
    while time.ticks_us()<t:
        pass
