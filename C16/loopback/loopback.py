from machine import UART,Pin
from utime import sleep_ms

uart=UART(1,baudrate=9600,bits=8,parity=2,rx=Pin(5),tx=Pin(4))
SendData = bytearray("A"*32,"utf-8")
uart.write(SendData)
sleep_ms(12)
RecData=uart.read(33)
print(RecData)
