#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:56:44 2022

@author: tamalaku\
"""
import os
import pandas as pd
import matplotlib.pyplot  as plt
import numpy as np
from scipy import stats
import statistics

length = 11.63


rep = 3

# data1 = pd.read_csv('boxone1.csv')
# A1 = data1['boxon1_0.csv']
# A2 = data1['boxon1_1.csv']
# A3 = data1['boxon1_2.csv']
# data1_average = (A1+A2+A3)/rep

data1 = pd.read_csv('boxone1.csv')
A1 = data1['boxon1_0.csv']
A2 = data1['boxon1_1.csv']
A3 = data1['boxon1_2.csv']
data1_average = (A1+A2+A3)/rep

data2 = pd.read_csv('boxon2.csv')
B1 = data2['boxon2_0.csv']
B2 = data2['boxon2_1.csv']
B3 = data2['boxon2_2.csv']
data2_average = (B1+B2+B3)/rep

velocity = length/len(A1)


data3 = pd.read_csv('boxoff1.csv')
K1 = data3['boxoff1_0.csv']
K2 = data3['boxoff1_1.csv']
K3 = data3['boxoff1_2.csv']
data3_average = (K1+K2+K3)/rep


C1 = data1_average-A1
C2 = data1_average-A2
C3 = data1_average-A3

D1 = data2_average-B1
D2 = data2_average-B2
D3 = data2_average-B3

compare_average =data1_average-data2_average





#%%
  
# # xaxis= np.arange(0,len(B1)) 
# plt.scatter(xaxis,B1,s=.1,label=1)
# plt.scatter(xaxis,B2,s=.1,label=2)
# plt.scatter(xaxis,B3,s=.1,label=3)
# plt.scatter(xaxis,data2_average,s=.1,label='Average')

xaxis= np.arange(0,len(B2)) 
plt.scatter(xaxis,B1,s=.1,label=1)
plt.scatter(xaxis,B2,s=.1,label=2)
plt.scatter(xaxis,B3,s=.1,label=3)
plt.scatter(xaxis,data2_average,s=.1,label='Average')

# plt.scatter(xaxis,compare_average,s=.1,label='Average')

plt.xlabel("Position (m)")
plt.ylabel("SNODAR_DISTANCE")
plt.legend(loc="lower center")
# plt.legend(loc="lower right")
# plt.title("Position Testing -  Average Minus Data Sets")
plt.title("Position Testing -  Average")

plt.savefig('Rotational_Comparison.png', dpi=300)



#%%
xaxis =  np.arange(0,len(C1))*velocity
plt.scatter(xaxis,C1,s=1,label=1)
plt.scatter(xaxis,C2,s=1,label=2)
plt.scatter(xaxis,C3,s=1,label=3)
# plt.scatter(xaxis,compare_average,s=1,label='Average')
# plt.scatter(xaxis,compare_average[0:-1],s=1,label='Average')

plt.xlabel("Position (m)")
plt.ylabel("SNODAR_DISTANCE")
plt.legend(loc="lower center")
# plt.legend(loc="lower right")
# plt.title("Position Testing -  Average Minus Data Sets")
plt.title("Average Minus Data Sets")

plt.savefig('Rotational_Comparison.png', dpi=300)

#%%
xaxis =  np.arange(0,len(D1))*velocity
plt.scatter(xaxis,D1,s=1,label=1)
plt.scatter(xaxis,D2,s=1,label=2)
plt.scatter(xaxis,D3,s=1,label=3)
# plt.scatter(xaxis,compare_average,s=1,label='Average')
# plt.scatter(xaxis,compare_average[0:-1],s=1,label='Average')

plt.xlabel("Position (m)")
plt.ylabel("SNODAR_DISTANCE")
plt.legend(loc="lower center")
# plt.legend(loc="lower right")
# plt.title("Position Testing -  Average Minus Data Sets")
plt.title("Average Minus Data Sets")

plt.savefig('Rotational_Comparison.png', dpi=300)


#%%

# fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2)
# ax1.scatter(xaxis,A1,s=.1,label=1)
# ax1.scatter(xaxis,A2,s =.1,label=1)
# ax1.scatter(xaxis,A3,s=.1,label=1)
# ax1.scatter(xaxis,data1_average,s=.1,label=1)
# ax2.scatter(xaxis,C1,s=.1,label=1)
# ax2.scatter(xaxis,C2,s=.1,label=1)
# ax2.scatter(xaxis,C3,s=.1,label=1)



#%% boxoff analysis 
xaxis =  np.arange(0,len(D1))*velocity
plt.scatter(xaxis,D1,s=1,label=1)
plt.scatter(xaxis,D2,s=1,label=2)
plt.scatter(xaxis,D3,s=1,label=3)


#%%


plt.xlabel("Position (m)")
plt.ylabel("SNODAR_DISTANCE")
plt.legend(loc="lower center")
# plt.legend(loc="lower right")
# plt.title("Position Testing -  Average Minus Data Sets")
plt.title("Position Testing -  Average")

plt.savefig('Rotational_Comparison.png', dpi=300)



#%% HistograM
AB = B1-B2 
AC = B1-B3
BC = B2-B3

plt.hist(D3)
plt.title("Average-3")
plt.xlabel("Contrast")
plt.ylabel("Quantity")


plt.savefig('histogram', dpi=300)


#%%Data Analysis 
# Trail = 1,2,3,average,1-2,1-3,2-3,average-1,average-2, average-3 
one = B1
two = B2
three = B3
average = data2_average
onetwo = abs(B1-B2)
onethree = abs(B1-B3)
twothree = abs(B2-B3)
averageone = abs(average-B1)
averagetwo = abs(average-B2)
averagethree = abs(average-B3)
Trail = (one,two,three,average,onetwo,onethree,twothree,averageone,averagetwo,averagethree)

a = {}
b = {}
for x in Trail:
    # print(np.median(x))
    # print(np.median(Trail[x]))
    # print(stats.mode(x))
    print(statistics.stdev(x))
    # print(statistics.variance(x))

#%% compare t1t2

plt.plot(data2_average-data3_average)

plt.xlabel("Position (m)")
plt.ylabel("SNODAR_DISTANCE")
plt.legend(loc="lower center")
# plt.legend(loc="lower right")
# plt.title("Position Testing -  Average Minus Data Sets")
plt.title("T2-M1")

plt.savefig('Rotational_Comparison.png', dpi=300)







