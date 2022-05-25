#!/usr/bin/env python
import psutil
import platform
import shutil
import pprint
import curses

def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])

    return uptime_seconds


print('Platform :', platform.processor(),'Uptime :', get_uptime())

listOfProcessNames = list()
# Iterate over all running processes
for proc in psutil.process_iter():
   # Get process detail as dictionary
   pInfoDict = proc.as_dict(attrs=['pid', 'name', 'cpu_percent'])
   # Append dict of process detail in list
   listOfProcessNames.append(pInfoDict)
pprint.pprint(listOfProcessNames);

while True:
   cpu=psutil.cpu_percent(interval=1)
   ram=psutil.virtual_memory().percent
   avail_ram=psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
   avail_ram = "{:.2f}".format(avail_ram)
   disk=  shutil.disk_usage('/')
   time=psutil.boot_time()
   print('CPU % ',cpu, 'MEM % ',ram, 'AVAIL %', avail_ram, 'DISK' , disk)