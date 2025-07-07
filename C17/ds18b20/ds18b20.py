import network
from machine import Pin, Timer
from time import sleep_ms
import urequests
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
  

wifi=setup("country", "ssid", "password")
print("Connected")
url = "http://192.168.253.75:8080"
ow = onewire.OneWire(Pin(2))
presence = ow.reset()
if presence:
    print("Device present")
else:
    print("No device")

DS = ds18x20.DS18X20(ow)
roms = DS.scan()

while True:
    DS.convert_temp()
    temp = DS.read_temp(roms[0])
    buf = str(temp).encode("utf-8")
    try:
        r = urequests.put(url, data=buf)
        r.close()
    except:
        print("Server Not Online")
    sleep_ms(500)

