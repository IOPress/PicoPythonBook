from utime import sleep_ms
from machine import Pin
import onewire

class DS18B20:
    def __init__(self,pin):
        self.ow=onewire.OneWire(Pin(pin))    
        
    def convert(self):
        self.ow.writebyte(0x44)
        for i in range(500):
            sleep_ms(10)
            if self.ow.readbit() == 1:
                j=i
                break
        return j
   
    def getTemp(self):
        if not self.ow.reset:
            return -1000
        self.ow.writebyte(0xCC)
        if self.convert()==500:
            return -3000
        self.ow.reset()
        self.ow.writebyte( 0xCC)
        self.ow.writebyte( 0xBE)
        data=bytearray(9)
        self.ow.readinto(data)
        if self.ow.crc8(data)!=0:
            return -2000
        t1 = data[0]
        t2 = data[1]
        temp1 = (t2 << 8 | t1)
        if t2 & 0x80:
            temp1=temp1 | 0xFFFF0000
        return temp1/16

dS18B20=DS18B20(2)
print(dS18B20.getTemp())
