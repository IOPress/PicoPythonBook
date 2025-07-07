import uasyncio
import network
import rp2
from machine import Pin, Timer
from time import sleep_ms
import onewire
import ds18x20

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

wifi = setup("country", "ssid", "password")

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
async def serve_client(reader,writer):
    print("client")
    print(await reader.read(512))
    DS.convert_temp()
    temp = DS.read_temp(roms[0])
    html=template.replace("<!--#temp-->",str(temp))
    headers = ("HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=UTF-8\r\n"
            "Server:Pico\r\n"
            f"Content-Length:{len(html)}\r\n\r\n"
            )
    buf = headers.encode("utf-8")+html.encode("utf-8")
    
    writer.write(buf)
    await writer.drain()
    writer.close()
    await writer.wait_closed()

async def main():
    await uasyncio.start_server(serve_client, '192.168.253.88', 80,backlog=5)
    while True:
        print("heartbeat")
        await uasyncio.sleep(1) 

uasyncio.run(main())