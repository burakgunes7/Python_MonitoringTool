#!/usr/bin/env python
import psutil
import platform


def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])

    return uptime_seconds


print('Platform :', platform.processor(),'Uptime :', get_uptime())

while True:
   cpu=psutil.cpu_percent(interval=1)
   ram=psutil.virtual_memory().percent
   avail_ram=psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
   disk= psutil.disk_usage('/')
   time=psutil.boot_time()
   print('CPU ',cpu, 'MEM ',ram, 'AVAIL', avail_ram, 'DISK ' , disk)


