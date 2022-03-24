#Magnetic reed switch reader for Pico
#Remember to use pull-up resistor when connecting :)
#4.7Kohm resistor used in testing.
#Open state == 0 from gpio
#Closed state == 1 from gpio

from machine import Pin, Timer
import time
import machine


class ReedSwitch:
    
    def __init__(self):
        self.self = self
        self.pin = machine.Pin(21, Pin.IN)
        
    def getState(self):
        return self.pin.value()
    
switch = ReedSwitch()

while True:
    state = switch.getState()
    if state < 1:
        print("Closed")
    elif state == 1:
        print("Open")
    else:
        print("Reading", state, "Did something go wrong? Value should be 1 or 0")
    time.sleep(1)
