import machine  
import os
import sdcard
cs = machine.Pin(9, machine.Pin.OUT)
spi = machine.SPI(1,
                  baudrate=100000,
                  polarity=0,
                  phase=0,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(10),
                  mosi=machine.Pin(11),
                  miso=machine.Pin(8))
sd = sdcard.SDCard(spi, cs)
os.VfsFat.mkfs(sd)
os.mount(sd,"/sd")
f=open("/sd/Hello.txt", "w")
f.write("Hello World!\r\n")
f.write("Some more data\r\n")
f.close()
f=open("/sd/Hello.txt", "r")
data = f.read()
print(data)