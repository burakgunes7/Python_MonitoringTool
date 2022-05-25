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
# Python Resources Monitoring Tool
"""
console.print(Markdown(MARKDOWN))

table.add_column("CPU", style="cyan")
table.add_column("MEM", style="magenta")
table.add_column("AVAIL MEM", style="cyan")


while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    avail_ram = psutil.virtual_memory().available * 100 / \
        psutil.virtual_memory().total
    avail_ram = "{:.2f}".format(avail_ram)
    disk = shutil.disk_usage('/')

    time = psutil.boot_time()
    table.add_row(f"% {cpu}", f"% {ram}",
                  f"% {avail_ram}")
    console.print(table)
