#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Shadowrun dice rolling utility, designed for use during live games for
performing quick success tests, with or without the Edge-related Rule of Six

This relies on the SuccessTest class in the dice module."""

#standard library modules
import tkinter as TK
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

st = SuccessTest
tk = TK.Tk
