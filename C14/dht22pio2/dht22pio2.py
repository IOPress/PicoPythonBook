import rp2
from machine import Pin

@rp2.asm_pio(set_init=(rp2.PIO.OUT_LOW,rp2.PIO.OUT_LOW),
              autopush=True, in_shiftdir=rp2.PIO.SHIFT_LEFT)
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
    wait(1, pin, 0) [25]
    in_(pins, 1)
    wait(0, pin, 0)
    jmp(y_dec, "bits")
      
    set(y, 7)
    label("check")
    wait(1, pin, 0)[25]
    set(pins,2)
    set(pins,0)
    in_(pins, 1)
    wait(0, pin, 0)
    jmp(y_dec, "check")
    push(block)
    wrap()


class DHT22():
    def __init__(self, gpio):
        self.sm = rp2.StateMachine(0, dht22, freq=490196,
                in_base=Pin(gpio), set_base=Pin(gpio),       
                                       jmp_pin=Pin(gpio))
        self.sm.active(1)

    def getReading(self):
        self.sm.put(500)
        data=0
        data = self.sm.get()
        byte1 = (data >> 24 & 0xFF)
        byte2 = (data >> 16 & 0xFF)
        byte3 = (data >> 8 & 0xFF)
        byte4 = (data & 0xFF)
        checksum = self.sm.get() & 0xFF
        self.checksum = (checksum == (byte1+byte2+byte3+byte4) & 0xFF)
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