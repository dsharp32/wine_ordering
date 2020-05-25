#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:25:59 2020

@author: Daniel Sharp
"""

def generate_po_ref():
    """
    Convert date and time to hexidecimal.

    Returns
    -------
    hexNum : TYPE Hexidecial Number
        DESCRIPTION. Last five characters of the current date and time in hexidecimal.

    """
    from datetime import datetime
 
    now = datetime.now()
    date_time = now.strftime("%d%m%Y%H%M%S")
    int_date_time = int(date_time)
    intNum = int_date_time
    po_ref = hex(intNum).upper()[-5:]
    
    return po_ref