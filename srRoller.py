#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Shadowrun dice rolling utility, designed for use during live games for
performing quick success tests, with or without the Edge-related Rule of Six

This relies on the SuccessTest class in the dice module."""

#standard library modules
from tkinter import *
import logging
#custom module
from dice.successtest import SuccessTest

# instantiate objects
st = SuccessTest()

# constants
# minimum/maximum window sizes
WIN_MINX = 440
WIN_MINY = 420

#geometry
GEOMETRY = str(WIN_MINX) + "x" + str(WIN_MINY)

#default settings
POOL = 5
THRESHOLD = st.AVERAGE
#default Edge/Rule of Six test
EDGE_DEFAULT = False

#authorship information
__author__ = "Andrew Miesem"
__credits__ = "Andrew Miesem"
__version__ = "0.1"
__email__ = "andrew.miesem@gmail.com"

# set up logging
logging.basicConfig(filename='srdice.log',level=logging.DEBUG,format='%(asctime)s [%(levelname)s] %(message)s')
logging.debug('-'*40)
logging.debug('srdice -- development version STARTED')

def placeholder(caller):
    """placeholder functio until individual functions are built"""
    message = 'placeholder event fired from {}'.format(caller)
    logging.debug(message)
    print(message)

roll_test = placeholder('roll_test')
file_reset = placeholder('file_reset')

if __name__ == '__main__':
    root = Tk()
    # root.attributes()
    # root.geometry(GEOMETRY)
    root.iconbitmap("icon/icon.ico")
    root.title("Shadowrun Success Test Generator")
    # root.resizable(width=False, height=False)
    # root.minsize(WIN_MINX,WIN_MINY)

    root.mainloop()
