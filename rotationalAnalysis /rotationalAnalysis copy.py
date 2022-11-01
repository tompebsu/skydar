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
length = 8*2

### Raspberry Pi 
pi_data= pd.read_csv("/Users/tamalaku/Documents/skydar/skydar_data/pi/distanceTime/rt_10_21_2022_T1_2.csv")
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
lidar= pd.read_csv("/Users/tamalaku/Documents/skydar/skydar_data/lidar/SNODAR-C5BA8EF761C6__21OCT2022-1000_THRU_21OCT2022-1115.csv")
# lidar= pd.read_csv("/Users/tamalaku/Documents/skydar/skydar_data/SNODAR-C5BA8EF761C6__03AUG2022-1600_THRU_03AUG2022-1616copy.csv")
##Afternoon Time
#lidar['Date'] = pd.to_datetime(lidar['DATE'])- pd.Timedelta(hours=12)
##Morning Time 
lidar['Date'] = pd.to_datetime(lidar['DATE'])
lidar['Time'] = lidar['Date'].dt.time

### Create New list from Initial to Final (1 sec)
even =np.arange(0,len(pi_data),2)
odd =np.arange(1,len(pi_data),2)
v={}
frame={}

reps = 3 

for i in range (reps):
    v[i] = (pd.DataFrame(columns=['NULL'],
                      index=pd.date_range(pi_data['Date'][even[i]], pi_data['Date'][odd[i]],
                                          freq='1S'))
            .between_time('03:00','12:50')
            .index.strftime('%Y-%m-%d %H:%M:%S')
            .tolist()
    )
    
    frame[i] = pd.DataFrame(v[i], columns = [str(i)])
    # frame[i] = frame



# for j in range (1,3):
#      frame[j] = pd.DataFrame(v[j], columns = [str(j)])

motion={}
for j in range (0,reps):
      frame[j] = pd.to_datetime(frame[j][str(j)])
      frame[j] = frame[j].dt.time
      motion[j] = pd.DataFrame(frame[j])

    

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
#%%
for a in range(0,reps):
    print(frame[a])
    print(lidar)
    # frame['Time'] =frame[a]
    # match[a] = pd.merge(frame['Time'],lidar[Min[a]:Max[a]], how='outer', indicator=True)
    match[a] = pd.merge(frame[a],lidar[Min[a]:Max[a]], how = 'outer', left_on=f'{a}', right_on='Time')
    test =match[a]
    ##fill NA with 0 
    #match[a]['SNODAR_DISTANCE_DOFF'] = match[a]['SNODAR_DISTANCE_DOFF'].fillna(1)
    print(match[a])
    ##interpolate NA
    match[a]['SNODAR_DISTANCE'] = match[a]['SNODAR_DISTANCE'].interpolate()
    #match[a]['SNODAR_DISTANCE'] = match[a]['SNODAR_DISTANCE']
    sort[a] = match[a].sort_values(by=['Time'])
#%%

xaxis={}
for s in range(0,reps):
    xaxis[s] = np.arange(0,len(sort[s]))

combine = pd.DataFrame()
for z in range(0,reps):
  #  # plt.scatter(xaxis[z],sort[z]['SNODAR_DISTANCE_DOFF'][Min[z]:Max[z]],s=1,label=z+1)
    plt.scatter(xaxis[z]*velocity,match[z]['SNODAR_DISTANCE'],s=1,label=z+1)
    # plt.gca().invert_yaxis()
    # plt.legend((sort[z]),
    #         ('1', '2', '3', '4', '5'),
    #         scatterpoints=1,
    #         loc='upper left',
    #         ncol=3,
    #         fontsize=8)

    # ax.legend([sort[z], line2, line3], ['label1', 'label2', 'label3'])


    T1 = pd.DataFrame(sort[z]['SNODAR_DISTANCE'])

    combine.loc[:,f'LDP_10_21_2022_{z}.csv'] = match[z]['SNODAR_DISTANCE']
    # x.to_csv(f'boxon1_{z}.csv')
combine.to_csv('LDP_10_21_2022_.csv')


###Create new csv file
# with open('Example.csv', 'w', newline = '') as csvfile:
#     my_writer = csv.writer(csvfile, delimiter = ' ')
#     my_writer.writerow(["Date", "temperature 1", "Temperature 2"])
# for y in range(0,reps):
#       with open('example.csv', 'a', newline = '') as csvfile:
#         my_writer = csv.writer(csvfile, delimiter = ' ')
#         my_writer.writerow(x[y])



# plt.gca().invert_yaxis()
plt.xlabel("Position (m)")
plt.ylabel("SNODAR_DISTANCE")
plt.legend(loc="lower center")
# plt.legend(loc="lower right")
plt.title("Position Testing - Interpolate")
# plt.title("Position Testing")

plt.savefig('Rotational2.png', dpi=300)

