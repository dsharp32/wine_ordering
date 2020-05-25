#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:49:40 2020

@author: Daniel Sharp
"""

def is_empty(any_structure):
    """
    Check if any container is empty.

    Parameters
    ----------
    any_structure : TYPE Any data container.
        DESCRIPTION. 

    Returns
    -------
    bool
        DESCRIPTION. True if container is empty. False if contains any data.

    """
    if any_structure:
        return False
    else:
        return True
