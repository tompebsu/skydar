#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 11:27:42 2022

@author: tamalaku
"""
import pandas as pd
import numpy as np
import csv
from datetime import datetime
import datetime as dt
import matplotlib.pyplot  as plt

length = 11.63 #meter


### Raspberry Pi 
pi_data= pd.read_csv("/Users/tamalaku/Documents/skydar/skydar_data/pi/distanceTime/rt_9_18_22_T1_A.csv")
# pi_data= pd.read_csv("/Users/tamalaku/Documents/skydar/skydar_data/timeData_8_3_copy.csv")
# m = pi_data['minute']
# s = pi_data['second']

pi_data['date']=pi_data['date'].map("{:02}".format)
pi_data['month']=pi_data['month'].map("{:02}".format)
pi_data['hour']=pi_data['hour'].map("{:02}".format)
pi_data['minute']=pi_data['minute'].map("{:02}".format)
pi_data['second']=pi_data['second'].map("{:02}".format)

pi_data['dateTime'] = pi_data[['date','month','year','hour','minute','second']].astype(str).agg('-'.join, axis=1) 
pi_data['Date'] = pd.to_datetime(pi_data['dateTime'],format='%d-%m-%y-%H-%M-%S') 
pi_data['Time'] = pi_data['Date'].dt.time
pi_data['minTotal'] = pi_data['Date'].diff()
total_time_travel = pi_data['minTotal'][1::2]
total_time_travel_s = pi_data['minTotal'][1::2].dt.total_seconds()

velocity = length/total_time_travel_s[1]

### Lidar
lidar= pd.read_csv("/Users/tamalaku/Documents/skydar/skydar_data/lidar/SNODAR-C5BA8EF761C6__18SEP2022-1055_THRU_18SEP2022-1245.csv")
# lidar= pd.read_csv("/Users/tamalaku/Documents/skydar/skydar_data/SNODAR-C5BA8EF761C6__03AUG2022-1600_THRU_03AUG2022-1616copy.csv")
##Afternoon Time
# lidar['Date'] = pd.to_datetime(lidar['DATE'])- pd.Timedelta(hours=12)
##Morning Time 
lidar['Date'] = pd.to_datetime(lidar['DATE'])
lidar['Time'] = lidar['Date'].dt.time

### Create New list from Initial to Final (1 sec)
even =np.arange(0,len(pi_data),2)
odd =np.arange(1,len(pi_data),2)
v={}

reps = 3

for i in range (reps):
    v[i] = (pd.DataFrame(columns=['NULL'],
                      index=pd.date_range(pi_data['Date'][even[i]], pi_data['Date'][odd[i]],
                                          freq='1S'))
            .between_time('03:00','12:00')
            .index.strftime('%Y-%m-%d %H:%M:%S')
            .tolist()
    )
    
    frame = pd.DataFrame(v[0], columns = [str(0)])
    frame[0] = frame

for j in range (1,reps):
    frame[j] = pd.DataFrame(v[j], columns = [str(j)])


for k in range (0,reps):
    frame[k] = pd.to_datetime(frame[k])
    frame[k] = frame[k].dt.time

#### Comparing time
time={}
Range={}

for t in range(0,reps):
    time[t] = (lidar['Date'] >= pi_data['Date'][even[t]]) & (lidar['Date'] <= pi_data['Date'][odd[t]])
    Range[t]= max(np.where(time[t]))
Min={}
Max = {}
for m in range(0,reps):
    Min[m] = min(Range[m])
    Max[m] = max(Range[m])


## for s in range(0,5):
##     xaxis[s] = np.arange(0,Max[s]-Min[s])

    


    
    
match={}
sort={}
###MATCH 
for a in range(0,reps):
    frame['Time'] =frame[a]
    match[a] = pd.merge(frame['Time'],lidar[Min[a]:Max[a]], how='outer', indicator=True)
    ##fill NA with 0 
    #match[a]['SNODAR_DISTANCE_DOFF'] = match[a]['SNODAR_DISTANCE_DOFF'].fillna(0)
   
    ##interpolate NA
   # match[a]['SNODAR_DISTANCE_DOFF'] = match[a]['SNODAR_DISTANCE_DOFF'].interpolate()
    sort[a] = match[a].sort_values(by=['Time'])

xaxis={}
for s in range(0,reps):
    xaxis[s] = np.arange(0,len(sort[s]))

for z in range(0,reps):
  #  # plt.scatter(xaxis[z],sort[z]['SNODAR_DISTANCE_DOFF'][Min[z]:Max[z]],s=1,label=z+1)
    plt.scatter(xaxis[z]*velocity,sort[z]['SNODAR_DISTANCE_DOFF'],s=1,label=z+1)
    # plt.gca().invert_yaxis()
    # plt.legend((sort[z]),
    #         ('1', '2', '3', '4', '5'),
    #         scatterpoints=1,
    #         loc='upper left',
    #         ncol=3,
    #         fontsize=8)

    # ax.legend([sort[z], line2, line3], ['label1', 'label2', 'label3'])

# plt.gca().invert_yaxis()
plt.xlabel("Position (m)")
plt.ylabel("SNODAR_DISTANCE_DOFF")
plt.legend(loc="lower right")
# plt.legend(loc="lower right")
plt.title("Position Testing")

plt.savefig('Rotational Test.png', dpi=300)

