#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:04:41 2022

@author: tamalaku
"""
import pandas as pd
import numpy as np
import csv
from datetime import datetime
import datetime as dt
import matplotlib.pyplot  as plt
length = 8*2

# df['ID'] = df['ID'].str.zfill(15)

pi_data= pd.read_csv("/Users/tamalaku/Documents/skydar/skydar_data/pi/piSensors/skydar_10_21_2022_2.csv")
# pi_data['date']=pi_data['date'].map("{:02}".format)
# pi_data['month']=pi_data['month'].map("{:02}".format)
# pi_data['hour']=pi_data['hour'].map("{:02}".format)
pi_data['minute']=pi_data['minute'].str.zfill(2)
pi_data['second']=pi_data['second'].str.zfill(2)
# format = “%D-%M-%Y-%h-%m-%s
pi_data['dateTime'] = pi_data[['date','month','year','hour','minute','second']].astype(str).agg(' '.join, axis=1)

# pd.to_datetime(pi_data,infer_datetime_format=True).strftime('%m/%d/%Y %H:%M')
##############################################################################################################################
pi_data['Date'] = pd.to_datetime(pi_data['dateTime'],format = '%d %m %y %H %M %S',errors="coerce")

# pi_data['Date'] = pd.to_datetime(pi_data['Date'])
pi_data['Time'] = pi_data['Date'].dt.time

                                  #,
#                                 infer_datetime_format = True, # can we force the formatting?
                                 # format='%d-%m-%y-%H-%M-%S'
#                                 ).strptime('%d-%m-%y-%H-%M-%S') 

# timestring = pi_data['dateTime'].astype(str)
# dt = datetime.strptime( pi_data['dateTime'], '%d-%m-%y-%H-%M-%S') # strip the time to accept the non-zeros
# corrected = datetime.strftime(dt, '%d-%m-%y-%H-%M-%S')



##############################################################################################################################
######################
# pi_data['Date'] = pd.to_datetime(pi_data['dateTime'])
# pi_data['Time'] = pi_data['Date'].dt.time
# pi_data['GARMIN_LIDAR'] = pi_data['checksum']


### 

Motor_Time= pd.read_csv("/Users/tamalaku/Documents/skydar/skydar_data/pi/distanceTime/rt_10_21_2022_T1_2.csv")
Motor_Time['date']=Motor_Time['date'].map("{:02}".format)
Motor_Time['month']=Motor_Time['month'].map("{:02}".format)
Motor_Time['hour']=Motor_Time['hour'].map("{:02}".format)
Motor_Time['minute']=Motor_Time['minute'].map("{:02}".format)
Motor_Time['second']=Motor_Time['second'].map("{:02}".format)

Motor_Time['dateTime'] = Motor_Time[['date','month','year','hour','minute','second']].astype(str).agg('-'.join, axis=1) 
Motor_Time['Date'] = pd.to_datetime(Motor_Time['dateTime'],format='%d-%m-%y-%H-%M-%S') 
Motor_Time['Time'] = Motor_Time['Date'].dt.time
Motor_Time['minTotal'] = Motor_Time['Date'].diff()
total_time_travel = Motor_Time['minTotal'][1::2]
total_time_travel_s = Motor_Time['minTotal'][1::2].dt.total_seconds()
velocity = length/total_time_travel_s[1]

even =np.arange(0,len(Motor_Time),2)
odd =np.arange(1,len(Motor_Time),2)

v={}
frame={}
reps = 3
for i in range (reps):
    v[i] = (pd.DataFrame(columns=['NULL'],
                      index=pd.date_range(Motor_Time['Date'][even[i]], Motor_Time['Date'][odd[i]],
                                          freq='1S'))
            .between_time('03:00','12:50')
            .index.strftime('%Y-%m-%d %H:%M:%S')
            .tolist()
    )
    
    frame[i] = pd.DataFrame(v[i], columns = [str(i)])
motion={}
for j in range (0,reps):
      frame[j] = pd.to_datetime(frame[j][str(j)])
      frame[j] = frame[j].dt.time
      motion[j] = pd.DataFrame(frame[j])




#### Comparing time
time={}
Range={}

for t in range(0,reps):
    time[t] = (pi_data['Date'] >= Motor_Time['Date'][even[t]]) & (pi_data['Date'] <= Motor_Time['Date'][odd[t]])
    Range[t]= max(np.where(time[t]))
Min={}
Max = {}
for m in range(0,reps):
    Min[m] = min(Range[m])
    Max[m] = max(Range[m])
    
    
    
    
match={}
sort={}
###MATCH 
#%%
for a in range(0,reps):

    # frame['Time'] =frame[a]
    # match[a] = pd.merge(frame['Time'],lidar[Min[a]:Max[a]], how='outer', indicator=True)
    match[a] = pd.merge(frame[a],pi_data[Min[a]:Max[a]], how = 'outer', left_on=f'{a}', right_on='Time')
    sort[a] = match[a].sort_values(by=['Time'])
    
xaxis={}
for s in range(0,reps):
    xaxis[s] = np.arange(0,len(sort[s]))

z=0
match[z]['ax'] = match[z]['ax'].interpolate()
plt.scatter(xaxis[z]*velocity,match[z]['ax'],s=1,label=z+1)
plt.gca().invert_yaxis()


x = np.arange(0,2436-1887)


    
