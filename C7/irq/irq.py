from machine import Pin

def HelloIRQ1(pin):
    print("IRQ1")
    
def HelloIRQ2(pin):
    print("IRQ2")

pin1=Pin(21,Pin.IN,Pin.PULL_UP)
pin2=Pin(22,Pin.IN,Pin.PULL_UP)

pin1.irq(HelloIRQ1,Pin.IRQ_RISING)
pin2.irq(HelloIRQ2,Pin.IRQ_RISING)
while(True):
    pass