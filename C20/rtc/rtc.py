import ntptime
from machine import RTC
import network
from machine import Pin, Timer
from time import sleep_ms
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
wifi=setup("GB", "dlink3", "hawkhawk")
print("Connected")
print(wifi.ifconfig())

ntptime.host="pool.ntp.org"
ntptime.timeout=1000
try:
    ntptime.settime()
except Exception:
    print("NTP server not available")
    pass
rtc = RTC()
print(rtc.datetime())
