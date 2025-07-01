import dht
from machine import Pin
import time

dht=dht.DHT22(Pin(2))
while True:
    dht.measure()
    temp=dht.temperature()
    print(temp)
    hum=dht.humidity()
    print(hum)
    time.sleep(1)
