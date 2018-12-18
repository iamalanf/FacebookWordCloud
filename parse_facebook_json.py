# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 20:25:10 2018

@author: Alan
"""

import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

with open('message.json', 'r') as f:
    my_dict = json.load(f)
type(my_dict)

a = my_dict.get('messages')

file = open('message_content.txt', 'w', encoding="utf-8")
a_count = 0
b_count = 0

#Create new dataframe
df = pd.DataFrame()

count = 0
# Go through each entry
for entry in a:
    message = entry.get('content')
    file.write(' %s ' % (message))
    count = count + 1
    
    # Convert entry to dataframe
    df_temp = pd.DataFrame([entry], columns=entry.keys())
    df = df.append(df_temp, ignore_index = True)
    
    if(entry.get('sender_name')=='Alan Flinton'):
        a_count = a_count + 1
    else:
        b_count = b_count + 1
        
    print('\rCount %i ' % (count), end='')
#     if a_count > 3:
#         break
print(a_count, b_count)
    
file.close()

# Save dataframe
df.to_csv('messages.csv')
# Make a backup of dataframe
df_backup = df