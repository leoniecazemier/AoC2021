# -*- coding: utf-8 -*-

# imported the requests library
import pandas as pd
import numpy as np

#part 1
data = pd.read_excel(r'C:\Users\leoni\Documents\Python Scripts\AOC 2021\Day1\input.xlsx', header=None)
dataNumpy = data.to_numpy()
dataDiff = np.diff(dataNumpy, axis=0)
findPos = np.where(dataDiff>0)
numPos = len(findPos[0])

#part 2
windowvals = np.empty([len(dataNumpy)-2,1])
for idx, val in enumerate(dataNumpy):
    if idx<2:
        continue
    else:
        windowvals[idx-2] = np.mean(dataNumpy[(idx-2):idx+1])
    
winDiff = np.diff(windowvals, axis=0)
findWinPos = np.where(winDiff>0)
numWinPos = len(findWinPos[0])  
  
        