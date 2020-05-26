#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 22:34:27 2020

@author: user
"""
import generate_date as gd
import os.path
import pathlib
import os
import shutil

date = gd.generate_date()

def move_files(company,po):
    
    filename = po[-12:]
    
    destination = os.path.join('Sent Orders', date, company)
  
    pathlib.Path(destination).mkdir(parents=True, exist_ok=True)
    
    destination = os.path.join('Sent Orders', date, company, filename)
    
    source = os.path.join('Draft Orders', date, company, filename)
    
    for item in source:
        shutil.copy(source, destination)
    
