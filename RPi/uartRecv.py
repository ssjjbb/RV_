#Get data from pico through UART

import time
import serial


ser = serial.Serial('/dev/ttyS0')

class uartRecv:
    def __init__(self):
        self.self = self
        self.ser = serial.Serial('/dev/ttyS0')
        self.rx_data = 0
        
    def readUart(self):
        self.rx_data = self.ser.read()
        time.sleep(0.03)
        data_left = self.ser.inWaiting()
        self.rx_data += self.ser.read(data_left)
        msg = str(self.rx_data, 'UTF-8')
        self.ser.write(self.rx_data)
        return msg
