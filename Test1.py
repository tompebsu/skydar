#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 12:17:57 2022

Mask time and data set 

@author: tamalaku
"""
import pandas as pd
import numpy as np
import csv
from datetime import datetime
import datetime as dt
import matplotlib.pyplot  as plt
# import math

A1 = pd.read_csv("/Users/tamalaku/Desktop/Test/A1.csv")
A2 = pd.read_csv("/Users/tamalaku/Desktop/Test/A2.csv")





A1['DATE'] = pd.to_datetime(A1['Date'])
A1['Time'] = A1['DATE'].dt.time

A2['DATE'] = pd.to_datetime(A2['Date'])
A2['Time'] = A2['DATE'].dt.time


match1 = A2.merge(A1, on='Time')
match2 = pd.merge(A1,A2, how='outer', indicator=True)
match2['Number'] = match2['Number'].fillna(0)
k = match2.sort_values(by=['Time'])

# xaxis = np.arange(0,len(A1))
xaxis = np.arange(0,len(k))

# B = A1.combine_first(A2)
# new = B['Number'].fillna(0)



#create a time interval
# l = (pd.DataFrame(columns=['NULL'],
#                   index=pd.date_range('2016-09-02T17:30:00Z', '2016-09-04T21:00:00Z',
#                                       freq='1T'))
#        .between_time('07:00','21:00')
#        .index.strftime('%Y-%m-%dT%H:%M:%SZ')
#        .index.strftime('%Y-%m-%dT%H:%M:%SZ')
#        .tolist()
# )

motorTime= pd.read_csv("/Users/tamalaku/Documents/skydar/skydar_data/8_5/timeData_8_5_copy.csv")
m = motorTime['minute']
s = motorTime['second']

motorTime['date']=motorTime['date'].map("{:02}".format)
motorTime['month']=motorTime['month'].map("{:02}".format)
motorTime['hour']=motorTime['hour'].map("{:02}".format)
motorTime['minute']=motorTime['minute'].map("{:02}".format)
motorTime['second']=motorTime['second'].map("{:02}".format)


# motorTime['dateTime'] = motorTime[['date','month','year','hour','minute','second']].astype(str).map("{:02}".format).agg('-'.join, axis=1) 
motorTime['dateTime'] = motorTime[['date','month','year','hour','minute','second']].astype(str).agg('-'.join, axis=1) 
motorTime['Date'] = pd.to_datetime(motorTime['dateTime'],format='%d-%m-%y-%H-%M-%S') 
motorTime['Time'] = motorTime['Date'].dt.time
motorTime['minTotal'] = motorTime['Date'].diff()
total_time_travel = motorTime['minTotal'][1::2]
total_time_travel_s = motorTime['minTotal'][1::2].dt.total_seconds()



### Lidar
lidar= pd.read_csv("/Users/tamalaku/Documents/skydar/skydar_data/8_5/SNODAR-C5BA8EF761C6__05AUG2022-1510_THRU_05AUG2022-1525.csv")
lidar['Date'] = pd.to_datetime(lidar['DATE'])- pd.Timedelta(hours=12)
lidar['Time'] = lidar['Date'].dt.time
# lidar['Velocity'] = lidar['Time']*distance

l = (pd.DataFrame(columns=['NULL'],
                  index=pd.date_range('2022-08-05T03:12:39', '2022-08-05T03:14:17',
                                      freq='1S'))
       .between_time('03:00','12:00')
       .index.strftime('%Y-%m-%d %H:%M:%S')
       .tolist()
)

l2 = (pd.DataFrame(columns=['NULL'],
                  index=pd.date_range('2022-08-05T03:14:55', '2022-08-05T03:16:33',
                                      freq='1S'))
       .between_time('03:00','12:00')
       .index.strftime('%Y-%m-%d %H:%M:%S')
       .tolist()
)

l3 = (pd.DataFrame(columns=['NULL'],
                  index=pd.date_range('2022-08-05T03:16:57', '2022-08-05T03:18:35',
                                      freq='1S'))
       .between_time('03:00','12:00')
       .index.strftime('%Y-%m-%d %H:%M:%S')
       .tolist()
)

l4 = (pd.DataFrame(columns=['NULL'],
                  index=pd.date_range('2022-08-05T03:18:56', '2022-08-05T03:20:34',
                                      freq='1S'))
       .between_time('03:00','12:00')
       .index.strftime('%Y-%m-%d %H:%M:%S')
       .tolist()
)

l5 = (pd.DataFrame(columns=['NULL'],
                  index=pd.date_range('2022-08-05T03:21:01', '2022-08-05T03:22:40',
                                      freq='1S'))
       .between_time('03:00','12:00')
       .index.strftime('%Y-%m-%d %H:%M:%S')
       .tolist()
)


# i = pd.DataFrame(l, columns = ['Time']) # number 
# l = pd.to_datetime(l)
# i = pd.DataFrame(l, columns = ['T'])
# i['Time'] = i['T'].dt.time

l = pd.DataFrame(l, columns = ['Date']) 
l['DATE'] = pd.to_datetime(l['Date'])
l['Time'] = l['DATE'].dt.time
# l = pd.to_datetime(l)
# l = l.dt.time

l2 = pd.DataFrame(l2, columns = ['Date']) 
l2['DATE'] = pd.to_datetime(l2['Date'])
l2['Time'] = l2['DATE'].dt.time

l3 = pd.DataFrame(l3, columns = ['Date']) 
l3['DATE'] = pd.to_datetime(l3['Date'])
l3['Time'] = l3['DATE'].dt.time

l4 = pd.DataFrame(l4, columns = ['Date']) 
l4['DATE'] = pd.to_datetime(l4['Date'])
l4['Time'] = l4['DATE'].dt.time

l5 = pd.DataFrame(l5, columns = ['Date']) 
l5['DATE'] = pd.to_datetime(l5['Date'])
l5['Time'] = l5['DATE'].dt.time


mask1 = (lidar['Date'] >= '2022-08-05 03:12:39') & (lidar['Date'] <= '2022-08-05 03:14:17')
maxV1 = max(np.where(mask1)[0])
minV1 = min(np.where(mask1)[0])
# v= lidar['Time'][minV1:maxV1]
# # m = pd.merge(l,v, how='outer', indicator=True)

j = lidar['Time'][minV1:maxV1]
# j = pd.DataFrame(j, columns = ['Time'])


mask2 = (lidar['Date'] >= '2022-08-05 03:14:55') & (lidar['Date'] <= '2022-08-05 03:16:33')
maxV2 = max(np.where(mask2)[0])
minV2 = min(np.where(mask2)[0])

mask3 = (lidar['Date'] >= '2022-08-05 03:16:57') & (lidar['Date'] <= '2022-08-05 03:18:35')
maxV3 = max(np.where(mask3)[0])
minV3 = min(np.where(mask3)[0])

mask4 = (lidar['Date'] >= '2022-08-05 03:18:56') & (lidar['Date'] <= '2022-08-05 03:20:34')
maxV4 = max(np.where(mask4)[0])
minV4 = min(np.where(mask4)[0])

mask5 = (lidar['Date'] >= '2022-08-05 03:21:01') & (lidar['Date'] <= '2022-08-05 03:22:40')
maxV5 = max(np.where(mask5)[0])
minV5 = min(np.where(mask5)[0])



xaxis1 = np.arange(0,maxV1-minV1)
xaxis2 = np.arange(0,maxV2-minV2)
xaxis3 = np.arange(0,maxV3-minV3)
xaxis4 = np.arange(0,maxV4-minV4)
xaxis5 = np.arange(0,maxV5-minV5)


match3 = pd.merge(l['Time'],lidar, how='outer', indicator=True)
match3['SNODAR_DISTANCE_DOFF'] = match3['SNODAR_DISTANCE_DOFF'].fillna(0)
k2 = match3.sort_values(by=['Time'])


match4 = pd.merge(l2['Time'],lidar, how='outer', indicator=True)
match4['SNODAR_DISTANCE_DOFF'] = match4['SNODAR_DISTANCE_DOFF'].fillna(0)
k3 = match4.sort_values(by=['Time'])

match5 = pd.merge(l3['Time'],lidar, how='outer', indicator=True)
match5['SNODAR_DISTANCE_DOFF'] = match5['SNODAR_DISTANCE_DOFF'].fillna(0)
k4 = match5.sort_values(by=['Time'])

match6 = pd.merge(l4['Time'],lidar, how='outer', indicator=True)
match6['SNODAR_DISTANCE_DOFF'] = match6['SNODAR_DISTANCE_DOFF'].fillna(0)
k5 = match6.sort_values(by=['Time'])

match7 = pd.merge(l5['Time'],lidar, how='outer', indicator=True)
match7['SNODAR_DISTANCE_DOFF'] = match7['SNODAR_DISTANCE_DOFF'].fillna(0)
k6 = match7.sort_values(by=['Time'])

plt.scatter(xaxis1,k2['SNODAR_DISTANCE_DOFF'][minV1:maxV1],s=1)
plt.scatter(xaxis2,k3['SNODAR_DISTANCE_DOFF'][minV2:maxV2],s=1)
plt.scatter(xaxis3,k4['SNODAR_DISTANCE_DOFF'][minV3:maxV3],s=1)
plt.scatter(xaxis4,k5['SNODAR_DISTANCE_DOFF'][minV4:maxV4],s=1)
plt.scatter(xaxis5,k6['SNODAR_DISTANCE_DOFF'][minV5:maxV5],s=1)






