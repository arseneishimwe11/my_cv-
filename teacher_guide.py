# Python code for PC/Raspberry Pi:
# !/usr/bin/env python3

import serial
import time
from os import system

if __name__ == "__main__":
    ser = serial.Serial(
        port="COM3",
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    ser.flush()
   

    while True:
        msg = input("$ ")
        msg_as_bytes = bytes(msg+"\n", "UTF-8")
        ser.write(msg_as_bytes)
        time.sleep(0.5)
        line = ser.readline().decode("utf-8").rstrip()
        #print(line)



