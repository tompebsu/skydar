#!/usr/bin/env python3
# -*- coding: utf-8 -*-



"""
Created on Wed Sep 28 15:56:44 2022

@author: tamalaku\
"""
#box off analysis 

import os
import pandas as pd
import matplotlib.pyplot  as plt
import numpy as np
from scipy import stats
import statistics

length = 11.63


rep = 3


data1 = pd.read_csv('boxoff1.csv')
A1 = data1['boxoff1_0.csv']
A2 = data1['boxoff1_1.csv']
A3 = data1['boxoff1_2.csv']
data1_average = (A1+A2+A3)/rep

data2 = pd.read_csv('boxone1.csv')
B1 = data2['boxon1_0.csv']
B2 = data2['boxon1_1.csv']
B3 = data2['boxon1_2.csv']
data2_average = (B1+B2+B3)/rep

velocity = length/740

C1 = data1_average-A1
C2 = data1_average-A2
C3 = data1_average-A3

##%
xaxis= np.arange(0,len(A2)) 
plt.scatter(xaxis*velocity,A1,s=.1,label=1)
plt.scatter(xaxis*velocity,A2,s=.1,label=2)
plt.scatter(xaxis*velocity,A3,s=.1,label=3)
plt.scatter(xaxis*velocity,data1_average,s=.1,label='Average')

# plt.scatter(xaxis,compare_average,s=.1,label='Average')

plt.xlabel("Position (m)")
plt.ylabel("SNODAR_DISTANCE")
plt.legend(loc="upper right")
# plt.legend(loc="lower right")
# plt.title("Position Testing -  Average Minus Data Sets")
plt.title("Position Testing -  Average")

plt.savefig('Rotational_Comparison.png', dpi=300)



#%%

xaxis= np.arange(0,len(A2)) 
plt.scatter(xaxis*velocity,C1,s=.1,label=1)
plt.scatter(xaxis*velocity,C2,s=.1,label=2)
plt.scatter(xaxis*velocity,C3,s=.1,label=3)

# plt.scatter(xaxis,compare_average,s=.1,label='Average')

plt.xlabel("Position (m)")
plt.ylabel("SNODAR_DISTANCE")
plt.legend(loc="upper right")
# plt.legend(loc="lower right")
# plt.title("Position Testing -  Average Minus Data Sets")
plt.title("Average Minus Data Sets")

plt.savefig('Rotational_Comparison.png', dpi=300)

#%% HistograM
AB = A1-A2 
AC = A1-A3
BC = A2-A3

plt.hist(C3)
plt.title("Average-3")
plt.xlabel("Contrast")
plt.ylabel("Quantity")


plt.savefig('histogram', dpi=300)


#%% compare off and on boxes 
T1 = A1-B1
T2 = A2-B2
T3 = A3-B3
# plt.scatter(xaxis*velocity,A1,s=.1,label=1)
# plt.scatter(xaxis*velocity,A2,s=.1,label=2)
# plt.scatter(xaxis*velocity,A3,s=.1,label=3)

# plt.scatter(xaxis*velocity,B1[0:741],s=.1,label=1)
# plt.scatter(xaxis*velocity,B2[0:741],s=.1,label=2)
# plt.scatter(xaxis*velocity,B3[0:741],s=.1,label=3)

# plt.scatter(xaxis*velocity,data1_average,s=.1,label=1)
# plt.scatter(xaxis*velocity,data2_average[0:741],s=.1,label=1)

diff = data1_average-data2_average[0:741]
plt.scatter(xaxis*velocity,diff,s=.1,label=1)




#%%Data Analysis 
# Trail = 1,2,3,average,1-2,1-3,2-3,average-1,average-2, average-3 
one = A1
two = A2
three = A3
average = data1_average
onetwo = abs(A1-A2)
onethree = abs(A1-A3)
twothree = abs(A2-A3)
averageone = abs(average-A1)
averagetwo = abs(average-A2)
averagethree = abs(average-A3)
Trail = (one,two,three,average,onetwo,onethree,twothree,averageone,averagetwo,averagethree)

a = {}
b = {}
# for x in Trail:
    # print(np.mean(x))
    # print(np.median(x))
    # print(stats.mode(x))
    # print(statistics.stdev(x))
    # print(statistics.variance(x))


#%%box plot
# DF = pd.DataFrame({'1-2': onetwo, '1-3': onethree,'2-3': twothree, })
# ax = DF[['1-2', '1-3', '2-3']].plot(kind='box', title='boxplot', showmeans=True)

DF = pd.DataFrame({'averageone': averageone, 'averagetwo': averagetwo,'averagethree': averagethree, })
ax = DF[['averageone', 'averagetwo', 'averagethree']].plot(kind='box', title='boxplot', showmeans=True)

plt.show()





