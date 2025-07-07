from machine import UART,Pin, mem32
from utime import sleep_ms, time_ns

def presence(uart):
    uart.init(baudrate=9600)
    uart.write(bytes([0xF0]))
    sleep_ms(20)
    buf = uart.read(1)
    uart.init(baudrate=115200)
    if buf[0] == 0xF0:
        return -1
    return 0

def writeByte(uart,byte):
    buf=[]
    for i in range(8):
        if byte & 1 == 1:
            buf.append(0xFF)
        else:
            buf.append(0x00)
        byte = byte >> 1
    uart.write(bytes(buf))
    sleep_ms(10)
    byte=uart.read(8)
        
def readByte(uart):
    byte = bytes([0xFF]*8)
    uart.write(byte)
    sleep_ms(10)
    byte = uart.read(8)
    result=0
    for b in byte:
        result=result>>1
        if b==0xFF:
            result=result|0x80
    return result


uart = UART(1,baudrate=115200,bits=8,parity=None,rx=Pin(5),tx=Pin(4) )
print(presence(uart))

presence(uart)
writeByte(uart, 0xCC)
writeByte(uart, 0x44)
sleep_ms(1000)
presence(uart)
writeByte(uart, 0xCC)
writeByte(uart, 0xBE)

data=[]
for i in range(9):
    data.append(readByte(uart))
    
t1 = data[0]
t2 = data[1]
temp1 = (t2 << 8 | t1)
if t2 & 0x80:
    temp1=temp1 | 0xFFFF0000
temp=temp1/16
print(temp)