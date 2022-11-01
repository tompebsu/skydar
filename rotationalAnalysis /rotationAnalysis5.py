#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 16:40:57 2022

@author: tamalaku
"""

import pandas as pd
import numpy as np
import csv
from datetime import datetime
import datetime as dt
import matplotlib.pyplot  as plt

distance = 2.83464 #(m)

motorTime= pd.read_csv("/Users/tamalaku/Documents/skydar/timeData_8_3_copy.csv")
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
lidar= pd.read_csv("/Users/tamalaku/Documents/skydar/SNODAR-C5BA8EF761C6__03AUG2022-1600_THRU_03AUG2022-1616.csv")
lidar['Date'] = pd.to_datetime(lidar['DATE'])- pd.Timedelta(hours=12)
lidar['Time'] = lidar['Date'].dt.time
# lidar['Velocity'] = lidar['Time']*distance


### Match
match1 = motorTime.merge(lidar, on='Time')
match2 = lidar.reset_index().merge(motorTime, on='Time').set_index('index')

mask1 = (lidar['Date'] >= '2022-08-03 04:03:20') & (lidar['Date'] <= '2022-08-03 04:04:59')
maxV1 = max(np.where(mask1)[0])
minV1 = min(np.where(mask1)[0])

mask2 = (lidar['Date'] >= '2022-08-03 04:05:15') & (lidar['Date'] <= '2022-08-03 04:06:54')
maxV2 = max(np.where(mask2)[0])
minV2 = min(np.where(mask2)[0])

mask3 = (lidar['Date'] >= '2022-08-03 04:07:15') & (lidar['Date'] <= '2022-08-03 04:08:54')
maxV3 = max(np.where(mask3)[0])
minV3 = min(np.where(mask3)[0])

mask4 = (lidar['Date'] >= '2022-08-03 04:09:50') & (lidar['Date'] <= '2022-08-03 04:11:29')
maxV4 = max(np.where(mask4)[0])
minV4 = min(np.where(mask4)[0])

mask5 = (lidar['Date'] >= '2022-08-03 04:12:01') & (lidar['Date'] <= '2022-08-03 04:13:39')
maxV5 = max(np.where(mask5)[0])
minV5 = min(np.where(mask5)[0])

xaxis1 = np.arange(0,maxV1-minV1)
xaxis2 = np.arange(0,maxV2-minV2)
xaxis3 = np.arange(0,maxV3-minV3)
xaxis4 = np.arange(0,maxV4-minV4)
xaxis5 = np.arange(0,maxV5-minV5)

# lidar['diff'] = lidar.set_index(['SNODAR_DISTANCE_DOFF'][minV1:maxV1]).subtract(lidar.set_index(['SNODAR_DISTANCE_DOFF'][minV2:maxV2]),fill_value=0)

# lidar['k'] = lidar['SNODAR_DISTANCE_DOFF'][minV1:maxV1]-lidar['SNODAR_DISTANCE_DOFF'][minV1:maxV1]

lidar['k'] = lidar['SNODAR_DISTANCE_DOFF'][minV1:maxV1].sub(lidar['SNODAR_DISTANCE_DOFF'][minV2:maxV2], fill_value=0)
a= lidar['SNODAR_DISTANCE_DOFF'][minV1:maxV1]
b = lidar['SNODAR_DISTANCE_DOFF'][minV2:maxV2]
c = lidar['SNODAR_DISTANCE_DOFF'][minV3:maxV3]
d = lidar['SNODAR_DISTANCE_DOFF'][minV4:maxV4]
e = lidar['SNODAR_DISTANCE_DOFF'][minV5:maxV5]

ab = np.array(a)-np.array(b)
ac = np.array(a)-np.array(c)
ad = np.array(a)-np.array(d)
# ae = np.array(a)-np.array(e)

# plt.plot(xaxis1,lidar['SNODAR_DISTANCE_DOFF'][minV1:maxV1],label="1")
# plt.plot(xaxis2,lidar['SNODAR_DISTANCE_DOFF'][minV2:maxV2],label="2")
# plt.plot(xaxis3,lidar['SNODAR_DISTANCE_DOFF'][minV3:maxV3],label="3")
# plt.plot(xaxis4,lidar['SNODAR_DISTANCE_DOFF'][minV4:maxV4],label="4")
# plt.plot(xaxis5,lidar['SNODAR_DISTANCE_DOFF'][minV5:maxV5],label="5")
# plt.gca().invert_yaxis()

plt.plot(ab,label="1-2")
plt.plot(ac,label="1-3")
plt.plot(ad,label="1-4")
plt.gca().invert_yaxis()


plt.xlabel("POSITION")
plt.ylabel("SNODAR_DISTANCE_DOFF")
plt.legend(loc="upper right")
plt.title("Diff from Trial 1 Invert (8/3)")

#testing 