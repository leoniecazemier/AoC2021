# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 22:18:06 2021

@author: leoni
"""

# imported the requests library
import pandas as pd
import numpy as np
from scipy import stats

# part 1
data = pd.read_csv(r'C:\Users\leoni\Documents\Python Scripts\AOC 2021\Day3\input.csv', header=None, dtype=str, names = ['input'] )
dataPrac = pd.read_csv(r'C:\Users\leoni\Documents\Python Scripts\AOC 2021\Day3\inputPractice.csv', header=None, dtype=str, names = ['input'] )

datSep = np.empty([1000, 12],dtype=int)
datPrac = np.empty([12, 5],dtype=int)

for idx_d in data.index:
    datSep[idx_d,:] = [int(i) for i in list(data['input'][idx_d])]
    
for idx_d in dataPrac.index:
    datPrac[idx_d,:] = [int(i) for i in list(dataPrac['input'][idx_d])]
    
# a= np.mean(datSep, axis = 0)   
modeRow = stats.mode(datSep)
modeRowstr = ''.join(str(modeRow[0]))
modeRowstr_a = modeRowstr[2:-2]
stripped = ''.join(modeRowstr_a.split())

decim1 = int(stripped, 2)

modeRow_no = 1-modeRow[0]
modeRowstr_1 = ''.join(str(modeRow_no[0]))
modeRowstr_1_a = modeRowstr_1[1:-1]
stripped_1= ''.join(modeRowstr_1_a.split())

decim2 = int(stripped_1,2)

answer = decim1*decim2
 
   
# part 2
datox = datSep
datco = datSep


ridx = 0
while datox.shape[0]>1:
    moderow_y = stats.mode(datox)
    #check for 50/50 splits
    testval = moderow_y[0][0][ridx]
    print(float(moderow_y[1][0][ridx]))
    print(datox.shape[0]/2)
    if float(moderow_y[1][0][ridx]) == (datox.shape[0]/2):
        testval = 1
    datox = np.delete(datox,np.where(datox[:,ridx] != testval),axis=0)
    ridx = ridx+1
    
ridx = 0
while datco.shape[0]>1:
    moderow_n = stats.mode(datco)
    antimoderow = 1-moderow_n[0][0]
    testval = antimoderow[ridx]
    print(float(moderow_n[1][0][ridx]))
    print(datco.shape[0]/2)
    if float(moderow_n[1][0][ridx]) == (datco.shape[0]/2):
        testval =0
    datco = np.delete(datco,np.where(datco[:,ridx]!=testval),axis=0)
    ridx = ridx+1

strox = ''.join(str(datox[0])) 
strox_snip= ''.join(strox[1:-1].split())   
strco = ''.join(str(datco[0])) 
strco_snip= ''.join(strco[1:-1].split())  

decim1 = int(strox_snip, 2)       
decim2 = int(strco_snip, 2)      

answer = decim1*decim2
    
    