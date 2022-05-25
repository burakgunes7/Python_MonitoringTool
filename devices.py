# import os
# import sys

# import psutil
# from psutil._common import bytes2human


# def main():
#     templ = "%-17s %8s %8s %8s %5s%% %9s  %s"
#     print(templ % ("Device", "Total", "Used", "Free", "Use ", "Type",
#                    "Mount"))
#     for part in psutil.disk_partitions(all=False):
#         if os.name == 'nt':
#             if 'cdrom' in part.opts or part.fstype == '':
#                 # skip cd-rom drives with no disk in it; they may raise
#                 # ENOENT, pop-up a Windows GUI error for a non-ready
#                 # partition or just hang.
#                 continue
#         usage = psutil.disk_usage(part.mountpoint)
#         print(templ % (
#             part.device,
#             bytes2human(usage.total),
#             bytes2human(usage.used),
#             bytes2human(usage.free),
#             int(usage.percent),
#             part.fstype,
#             part.mountpoint))


# if __name__ == '__main__':
#     sys.exit(main())


#!/usr/bin/env python
import sys
import psutil
import platform
import shutil
import pprint
import os
import time
from locale import THOUSEP
from click import style
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.markdown import Markdown
from psutil._common import bytes2human

console = Console()
custom_theme = Theme({"success": "green", "error": "bold red"})
table = Table()

MARKDOWN = """
# Python Disk Monitoring Tool
"""
console.print(Markdown(MARKDOWN))

table.add_column("Device", justify="middle", style="cyan")
table.add_column("Total", justify="middle", style="cyan")
table.add_column("Used", justify="middle", style="cyan")
table.add_column("Free", justify="middle", style="cyan")
table.add_column("Use", justify="middle", style="cyan")
table.add_column("Type", justify="middle", style="cyan")
table.add_column("Mount", justify="middle", style="cyan")

for part in psutil.disk_partitions(all=False):
    if os.name == 'nt':
        if 'cdrom' in part.opts or part.fstype == '':
            # skip cd-rom drives with no disk in it; they may raise
            # ENOENT, pop-up a Windows GUI error for a non-ready
            # partition or just hang.
            continue
    usage = psutil.disk_usage(part.mountpoint)
    # print(templ % (
    #     part.device,
    #     bytes2human(usage.total),
    #     bytes2human(usage.used),
    #     bytes2human(usage.free),
    #     int(usage.percent),
    #     part.fstype,
    #     part.mountpoint))
    time = psutil.boot_time()
    table.add_row(f"{part.device}", f"{bytes2human(usage.total)}",
                  f"{bytes2human(usage.used)}", f"{bytes2human(usage.free)}",
                  f"{int(usage.percent)}", f"{(part.fstype)}", f"{(part.mountpoint)}")

console.print(table)


# def get_uptime():
#       with open('/proc/uptime', 'r') as f:
#          uptime_seconds = float(f.readline().split()[0])
#       return uptime_seconds

# console.log('Platform :', platform.processor(),'Uptime :', get_uptime())

# listOfProcessNames = list()
#    # Iterate over all running processes
# for proc in psutil.process_iter():
#       # Get process detail as dictionary
#       pInfoDict = proc.as_dict(attrs=['pid', 'name', 'cpu_percent'])
#       # Append dict of process detail in list
#       listOfProcessNames.append(pInfoDict)
# console.log(listOfProcessNames);

# while True:
#       cpu=psutil.cpu_percent(interval=1)
#       ram=psutil.virtual_memory().percent
#       avail_ram=psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
#       avail_ram = "{:.2f}".format(avail_ram)
#       disk=  shutil.disk_usage('/')
#       time=psutil.boot_time()
#       console.log('CPU % ',cpu, 'MEM % ',ram, 'AVAIL %', avail_ram, 'DISK' , disk)
