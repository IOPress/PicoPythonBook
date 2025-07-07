import network
import socket
import rp2
from time import sleep_ms
from machine import Pin, Timer
import onewire
import ds18x20

import ssl

def setup(country, ssid, key):
    rp2.country(country)
    wifi=network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.disconnect()
    LED=Pin("LED", Pin.OUT)
    LED.high()
    timeout=20000
    wifi.connect(ssid,key)
    timer=Timer()
    timer.init(period=200, mode=Timer.PERIODIC, 
                            callback=lambda t:LED.toggle())
    s=0
    while timeout>0:
        s=wifi.status()
        if s==3 or s<0:
            break
        sleep_ms(100)
        timeout=timeout-100
    
    if(s<2):
        timer.init(period=1000, mode=Timer.PERIODIC,
                            callback=lambda t:LED.toggle())
    else:
        timer.deinit()
        LED.high()
    return wifi


wifi = setup("country", "ssid", "key")
print(wifi.ifconfig())

ow = onewire.OneWire(Pin(2))
presence = ow.reset()
if presence:
 print("Device present")
else:
 print("No device")

DS = ds18x20.DS18X20(ow)
roms = DS.scan()


template = """<!DOCTYPE html>
<html>
<head> <title>Temperature</title> </head>
<body> <h1>Current Temperature</h1>
Hello Pico W Server World <br/>
The Temperature is: <!--#temp--><br/>
</body>
</html>
"""

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setblocking(False)
s.bind(addr)
s.listen(0)
while True:
    print("doing something")
    try:
        cl, addr = s.accept()
    except(OSError):
        continue
    cl.setblocking(True)

    print('client connected from', addr)
    print(cl.recv(512))
    DS.convert_temp()
    temp = DS.read_temp(roms[0])

    html=template.replace("<!--#temp-->",str(temp))
    headers = ("HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=UTF-8\r\n"
            "Server:Pico\r\n"
            f"Content-Length:{len(html)}\r\n\r\n"
            )
    buf = headers.encode("utf-8")+html.encode("utf-8")
    
    cl.send(buf)
   
    cl.close()

s.close()