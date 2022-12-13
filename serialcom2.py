#!/usr/bin/env python
# -*- coding: utf-8 -*-
# lsusb to check device name
# dmesg | grep "tty" to find port name

import influxdb_client
import os
import time
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from smbus2 import SMBus
import serial
import time
import psutil

if __name__ == '__main__':

    print('Running. Press CTRL-C to exit.')
    token = "X8JLwsKQXCds9DOri0-U5ixsPh64Js9hQ6m08w30QWMm9Ci8K5VLyMxSKABIQpHL2Iu_tljM81JkEWvYy6Ds0A=="
    print(token)
    org = "mada.kasler@gmail.com"
    url = "https://us-east-1-1.aws.cloud2.influxdata.com"

    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    #from smbus2 import SMBus

    bucket = "monitoring"
    write_api = client.write_api(write_option=SYNCHRONOUS)
    with serial.Serial("/dev/ttyACM4", 9600, timeout=1) as arduino:
        time.sleep(0.1)  # wait for serial to open
        if arduino.isOpen():
            print("{} connected!".format(arduino.port))
            memory = 0
            cpu_percentage = 0

            try:
                while True:

                    cpu_percentage = psutil.cpu_percent(4)
                    memory = psutil.virtual_memory()
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

                    memory_str = "MEM USAGE" + str(memory) + "MB\n"
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

                    point = (
                        Point("measurement2")
                        .tag("tagname1", "tagvalue1")
                        .field("cpu_percentage", cpu_percentage)
                        .field("memory_total", memory[0])
                        .field("memory_available", memory[1])
                        .field("memory_percent", memory[2])
                        .field("memory_used", memory[3])
                        .field("memory_free", memory[4])
                        .field("cpu_times_user", cputimes[0])
                        .field("cpu_times_system", cputimes[1])
                        .field("cpu_times_idle", cputimes[2])
                        .field("cpu_times_interrupt", cputimes[3])
                        .field("cpu_times_dpc", cputimes[4])
                        .field("cpu_count", cpucount)
                        .field("cpu_stats", cpu_stats[1])
                        .field("cpu_freq_current", cpu_freq[0])
                        .field("cpu_freq_max", cpu_freq[2])
                        .field("swap_mem_total", swapmemory[0])
                        .field("swap_mem_free", swapmemory[2])
                        .field("bytes_sent", netiocounters[0])
                        .field("bytes_recv", netiocounters[1])

                    )

                    arduino.write(cpu_str.encode())
                    arduino.write(memory_str.encode())
                    # arduino.write(cputimes_str.encode())
                    # arduino.write(cpucount_str.encode())
                    # arduino.write(cpustats_str.encode())
                    # arduino.write(cpufreq_str.encode())
                    # arduino.write(swapmemory_str.encode())
                    # arduino.write(diskpartitions_str.encode())
                    # arduino.write(netiocounters_str.encode())
                    # arduino.write(netconnections_str.encode())
                    # arduino.write(temperatures_str.encode())
                    # arduino.write(fans_str.encode())
                    # arduino.write(battery_str.encode())
                    write_api.write(
                        bucket=bucket, org="mada.kasler@gmail.com", record=point)
                    time.sleep(5)
            except KeyboardInterrupt:
                print("KeyboardInterrupt has been caught.")
