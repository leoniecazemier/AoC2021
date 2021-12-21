# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:34:50 2021

@author: leoni
"""

# -*- coding: utf-8 -*-

# imported the requests library
import pandas as pd
import numpy as np

# part 1
data = pd.read_csv(r'C:\Users\leoni\Documents\Python Scripts\AOC 2021\Day2\input.csv', header=None, delim_whitespace=True)
# dataNumpy = data.to_numpy()

DistHoriz = 0
DistDepth = 0

for idx in data.index:
    Distance = data.iloc[idx,1]
    Direction = data.iloc[idx,0]
    if Direction == "forward":
        DistHoriz = DistHoriz + Distance
    elif Direction == "up":
        DistDepth  = DistDepth - Distance
    elif Direction == 'down': 
        DistDepth = DistDepth + Distance
        
answer = DistDepth * DistHoriz   


#part 2
DistHoriz = 0
DistDepth = 0
Aim = 0

for idx in data.index:
    Distance = data.iloc[idx,1]
    Direction = data.iloc[idx,0]
    if Direction == "forward":
        DistHoriz = DistHoriz + Distance
        DistDepth = DistDepth + (Aim*Distance)
    elif Direction == "up":
        Aim = Aim - Distance
    elif Direction == 'down': 
        Aim = Aim + Distance
  
answer = DistDepth * DistHoriz
        
  
    
  