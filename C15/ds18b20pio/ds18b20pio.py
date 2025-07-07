import rp2
from machine import Pin
from utime import sleep_ms

@rp2.asm_pio(set_init=rp2.PIO.OUT_HIGH, out_init=rp2.
                     PIO.OUT_HIGH, autopush=True,push_thresh=8)
def DS1820(): 
    wrap_target()   
    label("again")
    pull(block)
    mov(x, osr)
    jmp(not_x, "read")   
    label("write")
    set(pindirs, 1) 
    set(pins,0)
    label("loop1") 
    jmp(x_dec,"loop1")
    set(pindirs, 2) [31]
    wait(1, pin, 0) [31]
   
    pull(block)
    mov(x, osr)
    label("bytes1")
    pull(block)
    set( y, 7)    
    set(pindirs, 3) 
    label("bit1")
    set(pins, 0) [1]
    out(pins,1) [31]
    set(pins, 1) [20]
    jmp(y_dec,"bit1")
    jmp(x_dec,"bytes1")
    set(pindirs, 0) [31]
    jmp("again")

    label("read")
    pull(block)
    mov( x, osr)
    label("bytes2")
    set( y, 7)
    label("bit2")
    set(pindirs, 1) 
    set(pins, 0) [1]  
    set(pindirs, 0) [5]
    in_(pins,1) [10]   
    jmp(y_dec,"bit2")
    jmp(x_dec,"bytes2")
    wrap()

class DS18B20:
    def __init__(self,pin):
        self.sm=rp2.StateMachine(0,DS1820,freq=490196,              
                              set_base=Pin(2),out_base=Pin(2),
               in_base=Pin(2),out_shiftdir=rp2.PIO.SHIFT_RIGHT, 
                                 in_shiftdir=rp2.PIO.SHIFT_RIGHT)
        self.sm.active(1)

    def writeBytes(self, bytes, len):
        self.sm.put(250)
        self.sm.put(len-1)
        for i in range(len):
            self.sm.put(bytes[i])

    def readBytes(self,len):
        self.sm.put(0)
        self.sm.put(len-1)
        bytes=[]
        for i in range(len): 
            bytes.append(self.sm.get() >> 24)
        return bytes

    def getTemp(self):
        self.writeBytes([0xCC,0x44],2)
        sleep_ms(1000)
        self.writeBytes([0xCC,0xBE],2)
        data=self.readBytes(9)
        t1 = data[0]
        t2 = data[1]
        temp1 = (t2 << 8 | t1)
        if t2 & 0x80:
            temp1=temp1 | 0xFFFF0000
        return temp1/16
dS18B20=DS18B20(2)
print(dS18B20.getTemp())