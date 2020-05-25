#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:02:48 2020

@author: Daniel Sharp
"""

def coord(x, y, unit=1):
    """
    Converts pdf spacing co-ordinates to metric.

    """
    x, y = x * unit, y * unit
    return x, y