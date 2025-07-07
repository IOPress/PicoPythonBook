import network
import socket
from machine import Pin, Timer
from time import sleep_ms
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

wifi=setup("country", "ssid", "password")
print("Connected")
ai = socket.getaddrinfo("www.example.com", 443,socket.AF_INET)
addr = ai[0][-1]
s = socket.socket(socket.AF_INET)
s.connect(addr)
sslSock=ssl.wrap_socket(s)
request = b"GET / HTTP/1.1\r\nHost:example.com\r\n\r\n"
sslSock.write(request)
print(sslSock.recv(512).decode("utf-8"))