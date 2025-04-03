"""
This program is a timer with gui

Might want to use threads and time instead of asyncio
need to look further into it to know for sure.
"""
# pylint: disable=W0401, W0614, R0903
# WildImport Error Ignored due to me being lazy and not wanting to import every tkinter module
from tkinter import *
from tkinter import ttk
from async_tkinter_loop import async_handler, async_mainloop
import asyncio


main_window = Tk()

frame = ttk.Frame(main_window, height=500, width=700)
frame.pack()

class timerlabel:

    def __init__(self, parent):
        self.cc = 0
        self.ss = 0
        self.mm = 0
        self.hh = 0
        self.label = ttk.Label(parent, text=f"{self.hh:02}:{self.mm:.2}:{self.ss:.2}.{self.cc:.2}")

async_mainloop(main_window)
