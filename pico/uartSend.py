#Send data with UART from Pico to RPi
import os
import utime
import machine


class UartSender:
    def __init__(self):
        self.self = self
        self.uart = machine.UART(0, baudrate = 9600)
        self.data = 0
        
    def send(self, data):
        self.data = data
        self.uart.write(str(self.data))
        utime.sleep(1)
    
