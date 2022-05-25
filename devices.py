#!/usr/bin/env python
import sys
import psutil
import platform
import shutil
import pprint
import os
import time
import curses
from locale import THOUSEP
from click import style
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.markdown import Markdown
from psutil._common import bytes2human

os.system('cls' if os.name == 'nt' else 'clear')

console = Console()
custom_theme = Theme({"success": "green", "error": "bold red"})
table = Table()

MARKDOWN = """
# Python Disk Monitoring Tool
"""
console.print(Markdown(MARKDOWN))

table.add_column("Device", justify="center", style="cyan")
table.add_column("Total", justify="center", style="cyan")
table.add_column("Used", justify="center", style="cyan")
table.add_column("Free", justify="center", style="cyan")
table.add_column("Use", justify="center", style="cyan")
table.add_column("Type", justify="center", style="cyan")
table.add_column("Mount", justify="center", style="cyan")

for part in psutil.disk_partitions(all=False):
    if os.name == 'nt':
        if 'cdrom' in part.opts or part.fstype == '':
            continue
    usage = psutil.disk_usage(part.mountpoint)
    time = psutil.boot_time()
    table.add_row(f"{part.device}", f"{bytes2human(usage.total)}",
                  f"{bytes2human(usage.used)}", f"{bytes2human(usage.free)}",
                  f"{int(usage.percent)}", f"{(part.fstype)}", f"{(part.mountpoint)}")

console.print(table)
sys.stdin.read(1)
