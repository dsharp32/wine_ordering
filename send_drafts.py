#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 22:27:50 2020

@author: user
"""

import generate_date as gd
import send_loop as sl
import move_files as ml

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
            sl.send_loop(email, company, body,po,cc_email,bcc_email)
            
            ml.move_files(company, po)
    
    elif value == 'N':
        print('Orders not sent.')
        
    else:
        print('Invalid input. Please try again.')
        send_drafts(df)
    
    print('Ordering completed.\nHave a nice day!')
    
        