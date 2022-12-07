#!/usr/bin/env python
# -*- coding: utf-8 -*-
# lsusb to check device name
# dmesg | grep "tty" to find port name

import serial
import time
import test

if __name__ == '__main__':

    print('Running. Press CTRL-C to exit.')
    with serial.Serial("/dev/ttyACM4", 9600, timeout=1) as arduino:
        time.sleep(0.1)  # wait for serial to open
        if arduino.isOpen():
            print("{} connected!".format(arduino.port))
            memory = 0
            cpu_percentage = 0

            try:
                while True:

                    cpu_percentage = test.cpu_percent(4)
                    memory = test.virtual_memory()[2]
                    cputimes = psutil.cpu_times()
                    cpucount = psutil.cpu_count()
                    cpustats = psutil.cpu_stats()
                    cpufreq = psutil.cpu_freq()
                    swapmemory = psutil.swap_memory()
                    diskpartitions = psutil.disk_partitions(all=False)
                    netiocounters = psutil.net_io_counters()
                    netconnections = psutil.net_connections(kind='inet')
                    temperatures = psutil.sensors_temperatures()
                    fans = psutil.sensors_fans()
                    battery = psutil.sensors_battery()

                    memory_str = "MEMORY USAGE" + str(memory) + "MB\n"
                    cpu_str = "CPU USAGE:" + str(cpu_percentage) + "%\n"
                    cputimes_str = "CPU TIMES:" + str(cputimes) + "%\n"
                    cpucount_str = "CPU COUNT:" + str(cpucount) + "%\n"
                    cpustats_str = "CPU STATS:" + str(cpustats) + "%\n"
                    cpufreq_str = "CPU FREQ:" + str(cpufreq) + "%\n"
                    swapmemory_str = "SWAP MEM AVL:" + str(swapmemory) + "%\n"
                    diskpartitions_str = "DISKS AVL:" + \
                        str(diskpartitions) + "%\n"
                    netiocounters_str = "NET I/O:" + str(netiocounters) + "%\n"
                    netconnections_str = "NET CONN:" + \
                        str(netconnections) + "%\n"
                    temperatures_str = "TEMP:" + str(temperatures) + "%\n"
                    fans_str = "NET CONN:" + str(fans) + "%\n"
                    battery_str = "NET CONN:" + str(battery) + "%\n"

                    arduino.write(cpu_str.encode())
                    arduino.write(memory_str.encode())
                    arduino.write(cputimes_str.encode())
                    arduino.write(cpucount_str.encode())
                    arduino.write(cpustats_str.encode())
                    arduino.write(cpufreq_str.encode())
                    arduino.write(swapmemory_str.encode())
                    arduino.write(diskpartitions_str.encode())
                    arduino.write(netiocounters_str.encode())
                    arduino.write(netconnections_str.encode())
                    arduino.write(temperatures_str.encode())
                    arduino.write(fans_str.encode())
                    arduino.write(battery_str.encode())
            except KeyboardInterrupt:
                print("KeyboardInterrupt has been caught.")
