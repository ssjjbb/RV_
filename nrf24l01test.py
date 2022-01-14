"""Test for nrf24l01 module.  Portable between MicroPython targets."""

import usys
import ustruct as struct
import utime
from machine import Pin, SPI
from nrf24l01 import NRF24L01
from micropython import const

# Slave pause between receiving data and checking for further packets.
_RX_POLL_DELAY = const(25)
# Slave pauses an additional _SLAVE_SEND_DELAY ms after receiving data and before
# transmitting to allow the (remote) master time to get into receive mode. The
# master may be a slow device. Value tested with Pyboard, ESP32 and ESP8266.
_SLAVE_SEND_DELAY = const(5)

if usys.platform == "pyboard":
    cfg = {"spi": 2, "miso": "Y7", "mosi": "Y8", "sck": "Y6", "csn": "Y5", "ce": "Y4"}
elif usys.platform == "esp8266":  # Hardware SPI
    cfg = {"spi": 1, "miso": 12, "mosi": 13, "sck": 14, "csn": 4, "ce": 5}
elif usys.platform == "esp32":  # Software SPI
    cfg = {"spi": -1, "miso": 32, "mosi": 33, "sck": 25, "csn": 26, "ce": 27}
elif usys.platform == "rp2":  # PI PICO
    cfg = {"spi": 0, "miso": 4, "mosi": 7, "sck": 6, "csn": 14, "ce": 17}
else:
    raise ValueError("Unsupported platform {}".format(usys.platform))

# Addresses are in little-endian format. They correspond to big-endian
# 0xf0f0f0f0e1, 0xf0f0f0f0d2
pipes = (b"\xe1\xf0\xf0\xf0\xf0", b"\xd2\xf0\xf0\xf0\xf0")


def master(msg):
    csn = Pin(cfg["csn"], mode=Pin.OUT, value=1)
    ce = Pin(cfg["ce"], mode=Pin.OUT, value=0)
    if cfg["spi"] == -1:
        spi = SPI(-1, sck=Pin(cfg["sck"]), mosi=Pin(cfg["mosi"]), miso=Pin(cfg["miso"]))
        nrf = NRF24L01(spi, csn, ce, payload_size=4)
    else:
        nrf = NRF24L01(SPI(cfg["spi"]), csn, ce, payload_size=4)

    nrf.open_tx_pipe(pipes[1])
    nrf.open_rx_pipe(1, pipes[0])
    nrf.start_listening()

    num_needed = 10
    num_successes = 0
    num_failures = 0
    led_state = 0

    print("NRF24L01 master mode, sending %d packets..." % num_needed)

    while num_successes < num_needed and num_failures < num_needed:
        # stop listening and send packet
        nrf.stop_listening()
        millis = utime.ticks_ms()
        #led_state = max(1, (led_state << 1) & 0x0F)
        print("sending:", msg)
        
        try:
            #INT message type
            #nrf.send(struct.pack("ii", msg, led_state))
            #Float message type
            nrf.send(struct.pack("f", msg))
            
        except OSError:
            pass

        # start listening again
        nrf.start_listening()
        #msg = msg+1
        # wait for response, with 250ms timeout
        start_time = utime.ticks_ms()
        timeout = False
        while not nrf.any() and not timeout: # start time > 250
            if utime.ticks_diff(utime.ticks_ms(), start_time) > 250:
                timeout = True

        if timeout:
            print("failed, response timed out")
            num_failures += 1

        else:
            
            # recv packet
            #(got_millis,) = struct.unpack("i", nrf.recv())
            #Float
            (got_msg,) = struct.unpack("f", nrf.recv())

            # print response and round-trip delay
            print(
                "got response:",
                got_msg#,
                #"(delay",
                #utime.ticks_diff(utime.ticks_ms(), got_msg),
                #"ms)",
            )
            
            num_successes += 1
            #OTA BREAK POIS JOS USEAMPI VIESTI SAMAA DATAA TULOSSA
            break

        # delay then loop
        utime.sleep_ms(250)

    print("master finished sending; successes=%d, failures=%d" % (num_successes, num_failures))


def slave():
    csn = Pin(cfg["csn"], mode=Pin.OUT, value=1)
    ce = Pin(cfg["ce"], mode=Pin.OUT, value=0)
    if cfg["spi"] == -1:
        spi = SPI(-1, sck=Pin(cfg["sck"]), mosi=Pin(cfg["mosi"]), miso=Pin(cfg["miso"]))
        nrf = NRF24L01(spi, csn, ce, payload_size=4)
    else:
        nrf = NRF24L01(SPI(cfg["spi"]), csn, ce, payload_size=4)

    nrf.open_tx_pipe(pipes[1])
    nrf.open_rx_pipe(1, pipes[0])
    nrf.start_listening()

    print("NRF24L01 slave mode, waiting for packets... (ctrl-C to stop)")
    while True:
        #print(pipes)
        if nrf.any():
            #print("nrf.any()")
            while nrf.any():
                buf = nrf.recv()
                print(buf)
                #millis, led_state = struct.unpack("ii", buf)
                #Float
                msg = struct.unpack("f", buf)
                msg = msg[0]
                print("received: ", msg)
                #dekryptaus(millis)
                #for led in leds:
                #    if led_state & 1:
                #        led.on()
                #    else:
                #        led.off()
                #    led_state >>= 1
                utime.sleep_ms(_RX_POLL_DELAY)

            # Give master time to get into receive mode.
            utime.sleep_ms(_SLAVE_SEND_DELAY)
            nrf.stop_listening()
            try:
                #nrf.send(struct.pack("i", millis))
                #Float
                nrf.send(struct.pack("f", msg))
            except OSError:
                pass
            print("sent response")
            nrf.start_listening()


try:
    import pyb

    leds = [pyb.LED(i + 1) for i in range(4)]
except:
    leds = []

print("NRF24L01 test module loaded")
print("NRF24L01 pinout for test:")
print("    CE on", cfg["ce"])
print("    CSN on", cfg["csn"])
print("    SCK on", cfg["sck"])
print("    MISO on", cfg["miso"])
print("    MOSI on", cfg["mosi"])
print("run nrf24l01test.slave() on slave, then nrf24l01test.master() on master")
