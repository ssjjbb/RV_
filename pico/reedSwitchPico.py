import reedSwitch
import nrf24l01test
import time

sensor = reedSwitch.ReedSwitch()
state = sensor.getState()
temp = 2
while True:
    state = sensor.getState()
    if state == temp:
        time.sleep(2)
    elif state != temp:
        nrf24l01test.master(state)
        temp = state
    
        
    
