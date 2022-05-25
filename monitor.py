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
from rich import print
from rich.theme import Theme
from rich.table import Table
from rich.markdown import Markdown
from rich.padding import Padding
from psutil._common import bytes2human
from rich.layout import Layout

os.system('cls' if os.name == 'nt' else 'clear')

console = Console()
layout = Layout()
custom_theme = Theme({"success": "green", "error": "bold red"})


MARKDOWN = """
# Python Resources Monitoring Tool
"""


while True:

    console.print(Markdown(MARKDOWN))

    table = Table()
    table.add_column("CPU",justify="center" ,style="cyan")
    table.add_column("MEMORY", justify="center",style="magenta")
    table.add_column("AVAILABLE MEMORY",justify="center", style="cyan")

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    avail_ram = psutil.virtual_memory().available * 100 / \
        psutil.virtual_memory().total
    avail_ram = "{:.2f}".format(avail_ram)
    table.add_row(f"% {cpu}", f"% {ram}",
                  f"% {avail_ram}")
    console.print(Padding(table, (5, 30)))
    time.sleep(1.3)
    os.system('clear')
