import rp2
from machine import Pin

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW, autopush=True,   
                         in_shiftdir=rp2.PIO.SHIFT_RIGHT)
def dht22():
    wrap_target()
    label("again")
    pull(block)
    set(pins, 0)
    mov(x, osr)
    label("loop1")
    jmp(x_dec, "loop1")
    set(pindirs, 0)

    wait(1, pin, 0)
    wait(0, pin, 0)
    wait(1, pin, 0)
    wait(0, pin, 0)

    set(y, 31)
    label("bits")
    wait(1, pin, 0)
    set(x, 0)
    label("loop2")
    jmp(x_dec, "continue")
    label("continue")
    jmp(pin, "loop2")
    in_(x, 4)
    jmp(y_dec, "bits")

    set(y, 7)
    label("check")
    wait(1, pin, 0)
    set(x, 0)
    label("loop3")
    jmp(x_dec, "continue2")
    label("continue2")
    jmp(pin, "loop3")
    in_(x, 4)
    jmp(y_dec, "check")
    wrap()

class DHT22():
    def __init__(self, gpio):
        self.sm = rp2.StateMachine(0, dht22, 
                    freq=976562, in_base=Pin(gpio), 
                     set_base=Pin(gpio), jmp_pin=Pin(gpio))
        self.sm.active(1)

    def getByte(self):
        count = self.sm.get()
        byte = 0
        for i in range(8):
            byte = byte << 1
            if ((count >> i * 4) & 0x0F) > 8:
                byte = byte | 1
        return byte

    def getReading(self):
        self.sm.put(1000)
        byte1 = self.getByte()      
        byte2 = self.getByte()
        byte3 = self.getByte()
        byte4 = self.getByte()
        checksum = self.getByte()
        self.checksum =  (checksum == (byte1+byte2+byte3+byte4) & 0xFF)
        self.humidity = ((byte1 << 8) | byte2) / 10.0
        neg = byte3 & 0x80
        byte3 = byte3 & 0x7F
        self.temperature = (byte3 << 8 | byte4) / 10.0
        if neg > 0:
            self.temperature = -self.temperature


dht = DHT22(2)
dht.getReading()
print("Checksum", dht.checksum)
print("Humidity= ", dht.humidity)
print("Temperature=", dht.temperature)