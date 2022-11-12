#!/usr/bin/env python
# -*- coding: utf-8 -*-
# lsusb to check device name
#dmesg | grep "tty" to find port name

import serial,time
import psutil

if __name__ == '__main__':

    print('Running. Press CTRL-C to exit.')
    with serial.Serial("/dev/ttyACM4", 9600, timeout=1) as arduino:
        time.sleep(0.1) #wait for serial to open
        if arduino.isOpen():
            print("{} connected!".format(arduino.port))
            memory=0
            cpu_percentage = 0

            try:
                while True:

                 cpu_percentage = psutil.cpu_percent(4)
                 memory = psutil.virtual_memory()[2]
                 memory_str = "MEMORY USAGE" + str(memory) + "MB\n"
                 cpu_str = "CPU USAGE:" + str(cpu_percentage) + "%\n"

                 arduino.write(cpu_str.encode())
                 arduino.write(memory_str.encode())
            except KeyboardInterrupt:
                print("KeyboardInterrupt has been caught.")
