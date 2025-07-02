from machine import Pin,time_pulse_us
from utime import sleep_ms,sleep_us

class DHT22():
    def __init__(self,gpio):
        self.pin = Pin(gpio, mode=Pin.IN)
        self.checksum=0
        self.temperature=0
        self.humidity=0
        sleep_ms(1)

    def getReading(self):
        DHT=self.pin   
        DHT.init(mode=Pin.OUT,value=0)
        sleep_ms(1)
        DHT.init(mode=Pin.IN)        

        t=time_pulse_us(DHT, 1, 1000) 
        t=time_pulse_us(DHT, 1, 1000) 
        
        data = 0      
        for i in range(32):
            t=time_pulse_us(DHT, 1, 1000)
            data = data << 1
            data = data | (t > 50)    
        
        checksum=0
        for i in range(8):
            t=time_pulse_us(DHT, 1, 1000)
            checksum = checksum << 1
            checksum = checksum |(t > 50)
  
        byte1 = (data >> 24 & 0xFF)
        byte2 = (data >> 16 & 0xFF)
        byte3 = (data >> 8 & 0xFF)
        byte4 = (data & 0xFF)
        self.checksum=(checksum ==(byte1+byte2+byte3+byte4)&0xFF)
        self.humidity = ((byte1 <<8)| byte2) / 10.0
        neg = byte3 & 0x80
        byte3 = byte3 & 0x7F
        self.temperature =(byte3 << 8 | byte4) / 10.0
        if neg > 0:
            self.temperature = -self.temperature
dht=DHT22(2)
dht.getReading()
print("Checksum",dht.checksum)
print("Humidity= ", dht.humidity)
print("Temperature=", dht.temperature)