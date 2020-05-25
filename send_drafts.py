#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 22:27:50 2020

@author: user
"""

import generate_date as gd
import send_message_gmail as sm
import shutil
import os
import time

date = gd.generate_date()

def send_drafts(df):
    
    df.to_string(index=False)
    value = input("Send orders?: Y/N\n")
    value = value.upper()
    
    if value == 'Y':
        
        for i in range(len(df)):
            email = df.iloc[i, 0]
            company = df.iloc[i, 1]
            body = df.iloc[i, 2]
            po = df.iloc[i, 3]
            cc_email = df.iloc[i, 4]
            bcc_email = df.iloc[i, 5]
            
            print(f'Sending order to {company}')
            sm.send_message(email, company, body,po,cc_email,bcc_email)
            
        source = 'Draft Orders/'
        dest1 = 'Sent Orders/' + date + '/'

        files = os.listdir(source)

        for f in files:
            shutil.move(source+f, dest1)
        time.sleep(1)
        print('Ordering completed.\nHave a nice day!')  
    
    elif value == 'N':
        print('Orders not sent.')
        shutil.rmtree('Draft Orders/')
        
    else:
        print('Invalid input. Please try again.')
        send_drafts(df)