#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Shadowrun dice rolling utility, designed for use during live games for
performing quick success tests, with or without the Edge-related Rule of Six

This relies on the SuccessTest class in the dice module."""

#standard library modules
import tkinter as tk
#custom module
from dice.successtest import SuccessTest

#authorship information
__author__ = "Andrew Miesem"
__copyright__ = "Copyright 2017, Andrew Miesem"
__credits__ = "Andrew Miesem"
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Andrew Miesem"
__email__ = "andrew.miesem@gmail.com"
__status__ = "Development"

def placeholder(): print('placeholder event')
file_reset = placeholder

st = SuccessTest()
root = tk.Tk()
root.geometry('500x300')
root.resizable(width=False, height=True)
root.title('Shadowrun Dice Roller')

#application menu
menubar = tk.Menu(root)
root.config(menu=menubar)

filemenu = tk.Menu(menubar)
filemenu.add_command(label='Reset', command=file_reset)
filemenu.add_command(label='Exit', command=root.destroy)

menubar.add_cascade(label="File", menu=filemenu)

#application fields
tk.Label(root, text="Dice Pool").grid(row=0, sticky=tk.NE)
tk.Label(root, text="Threshold").grid(row=1, sticky=tk.NE)

pool = tk.Entry(root)
threshold = tk.Entry(root)

pool.grid(row=0,column=1)
threshold.grid(row=1,column=1)

root.mainloop()