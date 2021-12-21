# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 18:39:40 2021

@author: leoni
"""

import numpy as np
import numpy.matlib


fish = np.genfromtxt(r'C:\Users\leoni\Documents\Python Scripts\AOC 2021\Day6\input.csv',
                             delimiter= ',', encoding="utf-8-sig", dtype=int)

#part 1

fish = np.array([3,4,3,1,2])
day = 1

while day < 81:
    findBirths = np.where(fish == 0)
    numBirths = findBirths[0].shape[0]
    fish -= 1
    fish[findBirths[0]] = 6
    fish =  np.append(fish,np.tile(8,[numBirths,1]))
    day += 1
    
answer = len(fish)

#part 2
#(could be done as above but faster code is nicer)

fish = np.genfromtxt(r'C:\Users\leoni\Documents\Python Scripts\AOC 2021\Day6\input.csv',
                             delimiter= ',', encoding="utf-8-sig", dtype=int)
# fish = np.array([3,4,3,1,2])

def oneDay(numFish):
    newFish = np.zeros((9,1))
    numBirths = numFish[0]
    # go through cycle
    for idx in range(8):
        newFish[idx] = numFish[idx+1]
     #births
    newFish[6] = newFish[6]+numBirths
    newFish[8] = numBirths
    return newFish


numFish = np.zeros((9,1))
for idx in range(8):
    numFish[idx] = np.sum(fish == idx)

day = 1
while day < 257:
   numFish = oneDay(numFish)
   day += 1
    
answer = np.sum(numFish)