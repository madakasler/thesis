
from gpiozero import CPUTemperature
import psutil
import serial
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client import WritePrecision
from influxdb_client import Point
from influxdb_client import InfluxDBClient
from datetime import datetime
import time
import os
import influxdb_client
//PYTHON
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# lsusb to check device name
# dmesg | grep "tty" to find port name


if __name__ == '__main__':

    print('Running. Press CTRL-C to exit.')
    token = "X8JLwsKQXCds9DOri0-U5ixsPh64Js9hQ6m08w30QWMm9Ci8K5VLyMxSKABIQpHL2Iu_tljM81JkEWvYy6Ds0A=="
    print(token)
    org = "mada.kasler@gmail.com"
    url = "https://us-east-1-1.aws.cloud2.influxdata.com"

    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    if(client == None):
        print("Connection refused")
        exit
    #from smbus2 import SMBus

    bucket = "monitoring"
    write_api = client.write_api(write_option=SYNCHRONOUS)
    if(write_api == None):
        print("Communication protocol is not correct")
        exit
    # test the system first before sending data

    # if we don't do this, we might get false data in the system and that this will fail in influx.
    for x in range(5):
        psutil.cpu_percent(interval=1)

    for x in range(5):
        psutil.cpu_percent(interval=1, percpu=True)

    for x in range(5):
        psutil.cpu_times_percent(interval=1, percpu=False)

    val = psutil.getloadavg()  # also on Windows (emulated)
    print(val)

    disk = psutil.disk_usage('/')
    print(disk)

    net_iocounters = psutil.net_io_counters(pernic=True)
    print(net_iocounters)

    net_if_addrs = psutil.net_if_addrs()
    print(net_if_addrs)

    pids = psutil.pids()

    print(pids)

    # for proc in psutil.process_iter(['pid', 'name']):
    # print(proc.info)

    # print(list(psutil.win_service_iter()))

    with serial.Serial("/dev/ttyUSB0", 9600, timeout=1) as arduino:
        time.sleep(0.1)  # wait for serial to open
        if arduino.isOpen():
            print("{} connected!".format(arduino.port))
            memory = 0
            cpu_percentage = 0
            memory_str = "MEM USAGE:"
            cpu_str = "CPU USAGE:"
            cputimes_str = "CPU TIMES:"
            cpucount_str = "CPU COUNT:"
            cpustats_str = "CPU STATS:"
            cpufreq_str = "CPU FREQ:"
            swapmemory_str = "SWAP MEM AVL:"
            diskpartitions_str = "DISKS AVL:"
            netiocounters_str = "PCK_SNT"
            netconnections_str = "NET CONN:"
            temperatures_str = "CPU_TEMP:"
            fans_str = "FANS:"
            battery_str = "BATTERY:"

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
                    temperatures = CPUTemperature().temperature
                    fans = psutil.sensors_fans()
                    battery = psutil.sensors_battery()

                    memory_str = memory_str + str(memory[0]) + "MB\n"
                    cpu_str = cpu_str + str(cpu_percentage) + "%\n"
                    cputimes_str = cputimes_str + str(cputimes[1]) + "%\n"
                    cpucount_str = cpucount_str + str(cpucount) + "%\n"
                    cpustats_str = cpustats_str + str(cpustats[1]) + "%\n"
                    cpufreq_str = cpufreq_str + str(cpufreq[0]) + "%\n"
                    swapmemory_str = swapmemory_str + \
                        str(swapmemory[0]) + "%\n"
                    diskpartitions_str = diskpartitions_str + \
                        str(diskpartitions) + "%\n"
                    netiocounters_str = netiocounters_str + \
                        str(netiocounters[2]) + "%\n"
                    netconnections_str = netconnections_str + \
                        str(netconnections) + "%\n"
                    temperatures_str = temperatures_str + \
                        str(temperatures) + "%\n"
                    fans_str = fans_str + str(fans) + "%\n"
                    battery_str = battery_str + str(battery) + "%\n"

                    # Data validations
                    # Data validations
                    if memory[0] < 0:
                        print("Invalid memory value detected!")
                        pass

                    if cpu_percentage < 0 or cpu_percentage > 100:
                        print("Invalid CPU percentage value detected!")
                        pass

                    if cputimes[1] < 0 or cputimes[1] > 100:
                        print("Invalid CPU times value detected!")
                        pass

                    if cpucount < 0:
                        print("Invalid CPU count value detected!")
                        pass

                    if cpustats[1] < 0:
                        print("Invalid CPU stats value detected!")
                        pass

                    if cpufreq[0] < 0:
                        print("Invalid CPU frequency value detected!")
                        pass

                    if swapmemory[0] < 0:
                        print("Invalid swap memory value detected!")
                        pass

                    if any(partition.mountpoint == '' for partition in diskpartitions):
                        print("Invalid disk partition value detected!")
                        pass

                    if netiocounters[2] < 0:
                        print("Invalid network I/O counters value detected!")
                        pass

                    if len(netconnections) == 0:
                        print("No network connections detected!")
                        pass

                    if temperatures < 0:
                        print("Invalid CPU temperature value detected!")
                        pass

                    if not fans:
                        print("No fan information available!")
                        pass

                    if battery.percent < 0 or battery.percent > 100:
                        print("Invalid battery percentage value detected!")
                        pass

                    print(netiocounters[2])

                    point = (
                        Point("measurement3")
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
                        .field("cpu_stats", cpustats[1])
                        .field("cpu_freq_current", cpufreq[0])
                        .field("cpu_freq_max", cpufreq[2])
                        .field("swap_mem_total", swapmemory[0])
                        .field("swap_mem_free", swapmemory[2])
                        .field("bytes_sent", netiocounters[0])
                        .field("bytes_recv", netiocounters[1])

                    )

                    if point == None:
                        print("Point is not ready for sending data")

                    arduino.write(cpu_str.encode())
                    arduino.write(memory_str.encode())
                    arduino.write(cputimes_str.encode())
                    arduino.write(temperatures_str.encode())
                    print(cpu_str.encode())
                    print(memory_str.encode())
                    print(cputimes_str.encode())
                    print(temperatures_str.encode())
                    arduino.write(cpucount_str.encode())
                    arduino.write(cpustats_str.encode())
                    arduino.write(cpufreq_str.encode())
                    arduino.write(swapmemory_str.encode())
#                     arduino.write(diskpartitions_str.encode())
                    arduino.write(netiocounters_str.encode())
#                     arduino.write(netconnections_str.encode())
                    arduino.write(temperatures_str.encode())
#                     arduino.write(fans_str.encode())
#                     arduino.write(battery_str.encode())

                    cpu_percentage = 0
                    memory_str = "MEM USAGE:"
                    cpu_str = "CPU USAGE:"
                    cputimes_str = "CPU TIMES:"
                    cpucount_str = "CPU COUNT:"
                    cpustats_str = "CPU STATS:"
                    cpufreq_str = "CPU FREQ:"
                    swapmemory_str = "SWAP MEM AVL:"
                    diskpartitions_str = "DISKS AVL:"
                    netiocounters_str = "PCK_SNT"
                    netconnections_str = "NET CONN:"
                    temperatures_str = "CPU_TEMP:"
                    fans_str = "FANS:"
                    battery_str = "BATTERY:"
                    write_api.write(
                        bucket=bucket, org="mada.kasler@gmail.com", record=point)
                    if(write_api == None):
                        print("Bucket not found")
                    time.sleep(5)
            except KeyboardInterrupt:
                print("KeyboardInterrupt has been caught.")
        else:
            print("Arduino is not connected, try again")
