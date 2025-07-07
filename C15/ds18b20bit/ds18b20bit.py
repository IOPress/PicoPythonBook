from utime import sleep_ms, sleep_us
from machine import Pin
from time import sleep

class DS18B20:
    def __init__(self,pin):
        self.pin=Pin(pin,mode=Pin.IN)
        self.pin.high()
    
    def presence(self):
        self.pin.init(mode=Pin.OUT)
        self.pin.high()
        sleep_ms(1)
        self.pin.low()
        sleep_us(480)
        self.pin.init(mode=Pin.IN)
        sleep_us(70)
        b = self.pin.value()
        sleep_us(410)
        return b
        
    @micropython.native
    def writeBit(self,b):
        if b == 1:
            delay1 = 1
            delay2 = 30
        else:
            delay1 = 30
            delay2 = 0  
        self.pin.low()
        for i in range(delay1):
            pass
        self.pin.high()
        for i in range(delay2):
            pass

    def writeByte(self,byte):
        self.pin.init(mode=Pin.OUT)
        for i in range(8):
            self.writeBit(byte & 1)
            byte = byte >> 1
        self.pin.init(mode=Pin.IN)

    @micropython.native
    def readBit(self):
        self.pin.init(mode=Pin.OUT)
        self.pin.low()  
        self.pin.high() 
        self.pin.init(mode=Pin.IN)
        b = self.pin.value()
        sleep_us(60)
        return b

    def readByte(self):
        byte = 0
        for i in range(8):
            byte = byte | self.readBit() << i
        return byte
        
    def convert(self):
        self.writeByte(0x44)
        for i in range(500):
            sleep_ms(10)
            if self.readBit() == 1:
                j=i
                break
        return j

    def crc8(self,data,len):
        crc = 0
        for i in range(len):
            databyte = data[i]
            for j in range(8):
                temp = (crc ^ databyte) & 0x01
                crc >>= 1
                if temp:
                    crc ^= 0x8C
                databyte >>= 1
        return crc


    def getTemp(self):
        if self.presence()==1:
            return -1000
        self.writeByte(0xCC)
        if self.convert()==500:
            return -3000
        self.presence()
        self.writeByte( 0xCC)       
        self.writeByte( 0xBE)
        data=[]
        for i in range(9):
            data.append(self.readByte())
        if self.crc8(data,9)!=0:
            return -2000
        t1 = data[0]
        t2 = data[1]
        temp1 = (t2 << 8 | t1)
        if t2 & 0x80:
            temp1=temp1 | 0xFFFF0000
        return temp1/16



dS18B20=DS18B20(2)
if dS18B20.presence() == 1:
    print("No device")
else:
    print("Device present")

print(dS18B20.getTemp())
