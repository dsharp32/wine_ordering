#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:49:40 2020

@author: Daniel Sharp
"""

# Import libaries
import pandas as pd
import matplotlib.pyplot as plt

def generate_table(order):
    """
    Generate table from order dictionary. Calculate tax and insert total columns and rows.
    
    Parameters
    ----------
    order : TYPE Dictionary of lists.
        DESCRIPTION. Dict with order columns as keys, values are order "Units", "Product", "LUC".

    Returns
    -------
    total_cost : TYPE float.
        DESCRIPTION. Total cost of order inc tax.

    """
   
    df = pd.DataFrame.from_dict(order) # Create dataframe.
   
    df[['Units', 'LUC']] = df[['Units', 'LUC']].apply(pd.to_numeric) # Convert units & LUC to numeric type.
    df['Total ex GST'] = df['LUC'] * df['Units'] # Calculate product total ex GST.
    df[['Units', 'LUC', 'Total ex GST']] = df[['Units', 'LUC', 'Total ex GST']].apply(pd.to_numeric) 
    df['Total inc GST'] = df['LUC'] * df['Units'] * 1.1 # Calculate GST.
   
    df = df.round({'LUC': 2, 'Units': 0, 'Total ex GST': 2, 'Total inc GST':2}) # Round to two decimal places.
    df = df.set_index('Product')
   
    df.loc['Total'] = df[['Total ex GST', 'Total inc GST']].sum().reindex(df.columns, fill_value='') # Sum totals.
    df = df.round({'LUC': 2, 'Units': 0, 'Total ex GST': 2, 'Total inc GST':2}) #Round totals.
    df.reset_index(level=0, inplace=True) 
    df = df.set_index('Product')
    df.reset_index(level=0, inplace=True)
    total_cost = str(df.loc[df.index[-1], 'Total inc GST']) # Create total cost string.
  
    table = pd.DataFrame(df) # Plot dataframe as table.
    table = plt.table(cellText=df.values, colLabels=table.columns, loc='left',colColours=['darkorange']*df.shape[1], colWidths=[0.8,0.1,0.12,0.2,0.2])
    table.auto_set_font_size(False)
    table.set_fontsize(8) # Set font size to 8.
    plt.axis('off')
    plt.savefig('order.png', bbox_inches='tight') #Save order table as .png.
    plt.clf()
    
    return total_cost
