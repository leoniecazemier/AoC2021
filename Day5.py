# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 17:02:58 2021

@author: leoni
"""

# Part 1 + 2
# Load data 
import numpy as np
inpLines = np.genfromtxt(r'C:\Users\leoni\Documents\Python Scripts\AOC 2021\Day5\input1.csv',
                             delimiter= ',', encoding="utf-8-sig", dtype=int)

#draw lines

ventMap = np.zeros((1000,1000))

for idx in range(inpLines.shape[0]):
    x1, y1, x2, y2 = inpLines[idx,:]
    sortY = np.sort([y1,y2])
    sortX = np.sort([x1,x2])
    #if xs are the same
    if x1 == x2:
        ventMap[x1,sortY[0]:sortY[1]+1] += 1
    #if ys are the same
    elif y1 == y2:
        ventMap[sortX[0]:sortX[1]+1,y1] += 1
    else:
        yList = [*range(sortY[0],sortY[1]+1)]
        if y2<y1:
            yList = yList[::-1]
            
        xList = [*range(sortX[0],sortX[1]+1)]
        if x2<x1:
            xList = xList[::-1]
            
        for combix in range(sortX[1]-sortX[0] +1):
            ventMap[xList[combix],yList[combix]] += 1
        
            
Overlap = np.where(ventMap>1)        
answer = Overlap[0].shape[0] 