#DS18B20 temp reader


from machine import Pin, Timer
import machine, onewire, ds18x20, time
import time


class ds18b20:
    def __init__(self):
        self.self = self
        self.pin = machine.Pin(22)
        self.sensor = ds18x20.DS18X20(onewire.OneWire(self.pin))
        
    def getTemp(self):
        roms = self.sensor.scan()
        self.sensor.convert_temp()
        for rom in roms:
            return self.sensor.read_temp(rom)
        
    
temperatureSensor = ds18b20()

while True:
    print(round(temperatureSensor.getTemp(), 1), "C")
    time.sleep(2)
