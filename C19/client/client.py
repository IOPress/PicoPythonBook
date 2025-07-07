import uasyncio
from time import sleep_ms
from machine import Pin, Timer
import network
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

async def main():
    reader,writer= await uasyncio.open_connection("www.example.com",80)
    request = b"GET /index.html HTTP/1.1\r\nHost:example.org\r\n\r\n"
    writer.write(request)
    await writer.drain()
    print((await reader.read(512)).decode("utf-8"))
    reader.close()
wifi = setup("country", "ssid", "key")
print("Connected")
print(wifi.ifconfig())
uasyncio.run(main())