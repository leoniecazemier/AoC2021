# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 16:59:36 2021

@author: leoni
"""

#Part 1

import numpy as np

def checkBingo(inpCard,order):
    
    draws = 0
    bingo = 0
    bingoSz = (5,5)
    bingoBox = np.zeros(bingoSz)
    
    # find bingo 
    while bingo==0:
        newNum = order[draws]
        numPos = np.where(inpCard == newNum)
        if numPos[0].size > 0:
            bingoBox[numPos[0][0], numPos[1][0]] = 1
        sumRows = bingoBox.sum(axis=0)
        sumCols = bingoBox.sum(axis=1)
        allBingos = np.concatenate((sumRows,sumCols),axis=0)
        draws += 1
        if any(allBingos == 5):
            bingo = 1
            
    #calculate score
    bingoBoxFlat = bingoBox.flatten()
    inpCardFlat = inpCard.flatten()
    unmarked = np.where(bingoBoxFlat==0)
    unmarkedNo = inpCardFlat[unmarked]
    unmarkedSum = np.sum(unmarkedNo)
    return draws, newNum, unmarkedSum
    
   
# Load data and organise it
drawingOrder = np.genfromtxt(r'C:\Users\leoni\Documents\Python Scripts\AOC 2021\Day4\Input1-1.csv',
                             delimiter= ',', encoding="utf-8-sig", dtype=int)
bingoCardsFlat = np.genfromtxt(r'C:\Users\leoni\Documents\Python Scripts\AOC 2021\Day4\Input1-2.csv',
                             encoding="utf-8-sig", dtype=int)

bingoCards3D = np.reshape(bingoCardsFlat,(100,5,5))

drawsAll = np.empty([100,1])
cardLastDraw =np.empty([100,1])
multAns = np.empty([100,1])

#check bingo for all cards
for idx in range(bingoCards3D.shape[0]):
    drawsAll[idx], cardLastDraw[idx], multAns[idx] = checkBingo(bingoCards3D[idx,:,:], drawingOrder)

 
#compute answer
earliestTime = min(drawsAll)
earliestBingo = np.where(drawsAll == earliestTime)

lastVal = cardLastDraw[earliestBingo]
numAns = multAns[earliestBingo]
                 
answer = lastVal*numAns

#part 2

#compute answer
latestTime = max(drawsAll)
latestBingo = np.where(drawsAll == latestTime)

lastVal = cardLastDraw[latestBingo]
numAns = multAns[latestBingo]
                 
answer = lastVal*numAns


    




