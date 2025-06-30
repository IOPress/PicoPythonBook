from machine import Pin, SPI
# remove hash from comments to see CS in action
spi=SPI(0,sck=Pin(6),miso=Pin(4),mosi=Pin(7))
spi.init(baudrate=500_000,bits=8, polarity=0, phase=0,firstbit=SPI.MSB )
#CS=Pin(5,Pin.OUT)
#CS.high()

read=bytearray(3)
write=bytearray([0xAA,0xAA,0xAA])
#CS.low()
spi.write_readinto(write,read)
#CS.high()

print(read,write)
spi.deinit()
