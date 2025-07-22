import network
from machine import Pin, Timer
from time import sleep_ms
import rp2
import urequests

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
        print(s)
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

wifi = setup("country", "ssid", "password")
print("Connected")

url = "http://192.168.253.45:8080"
r = urequests.get(url)
print(r.content)
r.close()

buf = b'Hello World'
r = urequests.post(url,data = buf)
print(r.content)
r.close()

r = urequests.put(url,data = buf)
print(r.content)
r.close()

r = urequests.patch(url,data = buf)
print(r.content)
r.close()

r=urequests.head(url)
print(r.content)
print(r.headers)
r.close()

r=urequests.delete(url,data = buf)
print(r.content)
r.close()