#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:49:40 2020

@author: Daniel Sharp
"""
 
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import os.path
import pathlib
import os
import coord as cd


def generate_pdf(company, filename, full_name, mobile, email, date, notes):
    """
    Draws pdf document. Inserts details from spreadsheet.
    Self commenting.

    Returns
    -------
    None. Saves PO in Draft Orders folder.

    """
  
    pdf = os.path.join('Draft Orders', date, company)
  
    pathlib.Path(pdf).mkdir(parents=True, exist_ok=True)
  
    pdf = os.path.join('Draft Orders', date, company, filename + '.pdf')
  
    c = canvas.Canvas(pdf, bottomup=1)
 
    c.drawImage('order.png',42.5, 300, width=850, preserveAspectRatio=True, anchor='c')
 
    c.rect(15, 15, 565, 810, stroke=1, fill=0)
    c.rect(45, 240, 500, 400, stroke=1, fill=0)
    c.rect(45, 45, 500, 160, stroke=1, fill=0)
 
    c.setFont('Helvetica-Bold', 25)
 
    c.drawString(*cd.coord(125,279, mm), text='Purchase Order')
    
    c.drawString(*cd.coord(15,279, mm), text='DANS TEAROOMS')
 
    c.setFont('Helvetica-Bold', 14)
 
    # c.drawImage('Black logo - no background.png',40, 740, width=50, preserveAspectRatio=True, mask='auto', anchor='c')
 
    c.drawString(*cd.coord(15, 270, mm), text='57-97 Ploughshare St')
    c.drawString(*cd.coord(15, 265, mm), text='Trinity 2024')                                   
    c.drawString(*cd.coord(15, 260, mm), text='05 8060 9999')                                
    c.drawString(*cd.coord(15, 255, mm), text='danstearooms.com')
 
    c.drawString(*cd.coord(30, 215, mm), text=full_name)
    c.drawString(*cd.coord(30, 210, mm), text=company)                                  
    c.drawString(*cd.coord(30, 205, mm), text=mobile)                                
    c.drawString(*cd.coord(30, 200, mm), text=email)
 
    c.drawString(*cd.coord(132.5,215, mm), text='PO REF: ' + filename)
    c.drawString(*cd.coord(132.5,210, mm), text='DATE: ' + date)
 
    c.drawString(*cd.coord(25, 60, mm), text='DELIVERY INSTRUCTIONS:')
 
    c.setFont('Helvetica-Bold', 12)
 
    c.drawString(*cd.coord(30 ,120, mm), text='Notes:')
 
    c.setFont('Helvetica', 12)
 
    c.drawString(*cd.coord(30 ,115, mm), text='Please include PO reference on invoice.')
    c.drawString(*cd.coord(30 ,110, mm), text=notes)
 
    c.drawString(*cd.coord(25, 55, mm), text='Deliver between 10am & 5pm Monday - Friday')                                  
    c.drawString(*cd.coord(25, 50, mm), text='Use loading dock on Lens St')                                
    c.drawString(*cd.coord(25, 35, mm), text='For any issues please contact:')
    c.drawString(*cd.coord(25, 30, mm), text='dan@danstearooms.com')
 
    c.showPage()
    c.save()
