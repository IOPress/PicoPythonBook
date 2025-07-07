from machine import lightsleep, Pin
led = Pin("LED", Pin.OUT)
led.off()


lightsleep(2500)

led.on()

while(True):
    pass
#print("Back from lightsleep!")