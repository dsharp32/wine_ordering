#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:51:14 2020

@author: user
"""

import send_message_gmail as sm

def send_loop(email, company, body,po,cc_email,bcc_email):
    num_loops = 0
    try:
        sm.send_message(email, company, body,po,cc_email,bcc_email)
    except OSError:
        send_loop(email, company, body,po,cc_email,bcc_email)    
        if num_loops == 0:
            print('Almost there!')
        elif num_loops == 1:
            print('Sorry nobody made me a coffee today!')
        elif num_loops == 2:
            print('These machines take a while to warm up sometimes!')
        elif num_loops == 3:
            print('Better late than never I suppose!')
        else:
            print('Someone is going to be in a lot of trouble...')
        num_loops += 1    
        