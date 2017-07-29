#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Shadowrun dice rolling utility, designed for use during live games for
performing quick success tests, with or without the Edge-related Rule of Six

This relies on the SuccessTest class in the dice module."""

#standard library modules
import tkinter as tk
import logging
#custom module
from dice.successtest import SuccessTest

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

file_reset = roll_test = placeholder('roll_test')

if __name__ == '__main__':
    pass