from machine import UART,Pin, Timer
from utime import sleep_ms,sleep, time_ns
uart = UART(1,baudrate=1200,bits=8,parity=None,rx=Pin(5),tx=Pin(4),txbuf=256,rxbuf=16*1024)
#uart = UART(1,baudrate=1200,bits=8,parity=None,rx=Pin(5),tx=Pin(4),txbuf=16*1024,rxbuf=512)
test="A"*(257+32)
#test="A"*(1000)
s = time_ns()
uart.write(test)
print((time_ns()-s)/1000000)
""" sleep_ms(8333)
RecData = uart.read()
print(RecData)
print(len(RecData)) """