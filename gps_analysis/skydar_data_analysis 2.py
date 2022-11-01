#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 16:03:45 2022

@author: tamalaku
"""
import pandas as pd
# import csv

#GPS 

gps= pd.read_csv("/Users/tamalaku/Documents/skydar/SNODAR-C5BA8EF761C6__07JUL2022-1100_THRU_07JUL2022-1200.csv")

#GPS.columns
# GPS.columns[1]
# GPS.iloc[1, 0]

# GPS_time = GPS.iloc[:,14].astype(int)-60000-18
#GPS_time = GPS.iloc[:,14].astype(int)
# GPS_time = GPS_time.tolist()


gps['Time'] = pd.to_datetime(gps['173515.00'],format='%H%M%S') - pd.Timedelta(hours=6) - pd.Timedelta(seconds=18)
gps['Time'] = gps['Time'].dt.time
#GPS_time = timeDF.tolist()

# GPS_time.astype(int)
# GPS_time['Time'] = pd.to_datetime(GPS_time['173515.00'])


#Lidar

# lidar= pd.read_csv("/Users/tamalaku/Documents/skydar/SNODAR-C5BA8EF761C6__22JUN2022-1140_THRU_22JUN2022-1146.csv")
# lidar['Date'] = pd.to_datetime(lidar['DATE'])
# lidar['Time'] = lidar['Date'].dt.strftime("%H:%M:%S").str.replace(':','')
# #lidar['Time4'] = lidar['Time3'].str.replace(':','')

# #Lidar_time = lidar.iloc[:,34]
# Lidar_time = lidar['Time'].astype(int)

lidar= pd.read_csv("/Users/tamalaku/Documents/skydar/SNODAR-C5BA8EF761C6__22JUN2022-1140_THRU_22JUN2022-1146.csv")
lidar['Date'] = pd.to_datetime(lidar['Date'])
lidar['Time'] = lidar['Date'].dt.time

# Merge the two DF
match = gps.merge(lidar, on='Time')
match