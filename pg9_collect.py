import machine
import dht
import time

d = dht.DHT11(machine.Pin(0))
with open("data.txt", "w") as f:
    f.write("temperature,humidity\n")
    i = 10
    while i >= 0:
        d.measure()
        t = d.temperature()
        h = d.humidity()
        f.write(f"{t},{h}\n")
        i = i - 1
        time.sleep(1)
