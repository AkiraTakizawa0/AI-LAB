import machine
import dht
import time

d = dht.DHT11(machine.pin(0))
m = -2.8212674826885054
c = 151.34381063636422

while True:
    d.measure()
    t = d.temperature()
    h = d.humidity()
    ph = m * t + c
    print(f"Temperature {t}C Humidity {h}% Predicted Humidity {ph}%")
    time.sleep(1)