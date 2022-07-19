# RV_
RV IoT project repo Adding some 'smart' sensors into RV to monitor temperature in the cabin and in the fridge (some alert for fridge temperature tresholds) and magnetic reed switches for all the hatches to monitor their open/closed state.

Project utilizes Raspberry Pi 4 as a controller unit with a touchscreen display situated somewhere on the dashboard of the vehicle. Sensors will be operating on Raspberry Pi Picos and communication between Picos is done via nRF24L01+ rf transceivers and Pico - RPi through UART. If wifi is available in the RV, might change Picos to ESP32 or similar mcu with built-in wifi support


