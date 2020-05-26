#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:05:47 2020

@author: user
"""
import ezgmail

def send_message(email, company, body,po,cc_email,bcc_email): 
    """

    """
    ezgmail.send(email, 'Order for ' + company, body, [po],cc=cc_email, bcc=bcc_email)