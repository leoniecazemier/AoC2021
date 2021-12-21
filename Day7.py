# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 20:41:08 2021

@author: leoni
"""

import numpy as np

positions = np.genfromtxt(r'C:\Users\leoni\Documents\Python Scripts\AOC 2021\Day7\input.csv',
                             delimiter= ',', encoding="utf-8-sig", dtype=int)

#part 1
fuelUsage = np.empty((2000,1))

for goalPos in range(2000):
    absDists = abs(positions-goalPos)
    fuelUsage[goalPos] = sum(absDists)
    
answer = min(fuelUsage)

#part 2  --- not sure how to do this most efficiently

def gsum(inp):
    nums = (inp*(inp+1))/2
    return nums


fuelUsage = np.empty((2000,1))

for goalPos in range(2000):
    temp = np.empty((positions.shape[0],1))
    
    for idx, realPos in enumerate(positions):
        temp[idx] = gsum(abs(realPos-goalPos))

    fuelUsage[goalPos] = sum(temp)
    
answer = min(fuelUsage)

    