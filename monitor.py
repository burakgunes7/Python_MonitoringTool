#!/usr/bin/env python3
import psutil
import os
import time
from psutil._common import bytes2human
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.markdown import Markdown
from rich.padding import Padding
from rich.layout import Layout

os.system('cls' if os.name == 'nt' else 'clear')

console = Console()
layout = Layout()
custom_theme = Theme({"success": "green", "error": "bold red"})

MARKDOWN = """
# Python Resource Monitoring Tool
"""


while True:
    table = Table()
    table2 = Table()

    table.add_column("CPU", justify="center", style="cyan")
    table.add_column("MEMORY", justify="center", style="magenta")
    table.add_column("AVAILABLE MEMORY", justify="center", style="cyan")

    table2.add_column("Device", justify="center", style="cyan")
    table2.add_column("Total", justify="center", style="cyan")
    table2.add_column("Used", justify="center", style="cyan")
    table2.add_column("Free", justify="center", style="cyan")
    table2.add_column("Use", justify="center", style="cyan")
    table2.add_column("Type", justify="center", style="cyan")
    table2.add_column("Mount", justify="center", style="cyan")

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    avail_ram = psutil.virtual_memory().available * 100 / \
                psutil.virtual_memory().total
    avail_ram = "{:.2f}".format(avail_ram)
    table.add_row(f"% {cpu}", f"% {ram}",
                  f"% {avail_ram}")
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                continue
        usage = psutil.disk_usage(part.mountpoint)
        table2.add_row(f"{part.device}", f"{bytes2human(usage.total)}",
                      f"{bytes2human(usage.used)}", f"{bytes2human(usage.free)}",
                      f"{int(usage.percent)}", f"{part.fstype}", f"{part.mountpoint}")
    os.system('clear')
    console.print(Markdown(MARKDOWN))
    console.print(Padding(table, (0, 72)))
    console.print(Padding(table2, (0, 50)))
    time.sleep(2)
