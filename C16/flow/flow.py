from machine import UART,Pin, Timer
from utime import sleep_ms,sleep, time_ns


uart = UART(1,baudrate=9600,bits=8,parity=None,rx=Pin(5),tx=Pin(4),rts=Pin(7),cts=Pin(6), timeout=0,timeout_char=0, txbuf=2000,rxbuf=128,flow=UART.RTS|UART.CTS)

test = "A"*1000
s = time_ns()
uart.write(test)
print((time_ns()-s)/1000000)
RecData = bytes()
while len(RecData)<1000:
    sleep_ms(500)
    if uart.any():
            RecData = RecData + uart.read()
            print(RecData)
            print(len(RecData))