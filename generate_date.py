#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 22:06:45 2020

@author: Daniel Sharp
"""

from datetime import datetime

def generate_date():
    """
    

    Returns
    -------
    date : TYPE String
        DESCRIPTION. Current date.

    """
 
    now = datetime.now() # current date and time
    date = now.strftime("%d-%m-%Y")
    date = str(date)
    return date
