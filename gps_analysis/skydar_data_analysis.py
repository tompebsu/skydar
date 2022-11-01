#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 16:03:45 2022

@author: tamalaku
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from geopy import Point, distance
# import csv

#GPS 

gps= pd.read_csv("/Users/tamalaku/Documents/skydar/skydar_data/data.csv")



gps['Time'] = pd.to_datetime(gps['173515.00'],format='%H%M%S') - pd.Timedelta(hours=6) - pd.Timedelta(seconds=18)
gps['Time'] = gps['Time'].dt.time

lidar= pd.read_csv("/Users/tamalaku/Documents/skydar/skydar_data/SNODAR-C5BA8EF761C6__22JUN2022-1140_THRU_22JUN2022-1146.csv")
lidar['Date'] = pd.to_datetime(lidar['DATE'])
lidar['Time'] = lidar['Date'].dt.time

# Merge the two DF

match = gps.merge(lidar, on='Time', right_index = True)
match = lidar.reset_index().merge(gps, on='Time').set_index('index')
latitude = match.iloc[:,15]
longitude= match.iloc[:,17]
altitude = match.iloc[:,22]
height = match.iloc[:,24]
distance = match.iloc[:,49]
a_x = match.iloc[:,7]
a_y = match.iloc[:,8]
a_z = match.iloc[:,9]
g_x = match.iloc[:,10]
g_y = match.iloc[:,11]
g_z = match.iloc[:,12]


# lat = np.empty(len(latitude))
###
lats_con = []
for i, l in enumerate(latitude):

    deg = str(l)[:2]
    dec_s = str(l)[2:].replace('.','')
    dec = str(float(dec_s)/60).replace('.','')
    lats_con.append(f'{deg}.{dec}')
    
    
for i in range(0, len(lats_con)):
    lats_con[i] = float(lats_con[i])
    
longs_con = []
for j, lo in enumerate(longitude):

    # deg2 = str(-1*lo)[:4]
    deg2 = str(lo)[:3]
    dec_s2 = str(lo)[3:].replace('.','')
    dec2 = str(float(dec_s2)/60).replace('.','')
    longs_con.append(f'{deg2}.{dec2}')
                     
for i in range(0, len(longs_con)):
    longs_con[i] = float(longs_con[i])
    ###
    
# k =open("/Users/tamalaku/Documents/skydar/gps.csv",'w')
# lats_con = lats_con.T
# k.write(str(lats_con))
# # k.write('\n')
# # k.write(str(longs_con))
# k.close()


# csv_table = np.genfromtxt("/Users/tamalaku/Documents/skydar/gps.csv")
# transposed = csv_table.T
# np.savetxt("table.csv", transposed, fmt="%i")
# k.close()

# ax = plt.axes(projection='3d')
# ax.plot3D(longs_con,lats_con,distance)

lats = []
for i, l in enumerate(gps.iloc[:,15]):

    deg = str(l)[:2]
    dec_s = str(l)[2:].replace('.','')
    dec = str(float(dec_s)/60).replace('.','')
    lats.append(f'{deg}.{dec}')
# lats = lats.astype(float)
    
for i in range(0, len(lats)):
    lats[i] = float(lats[i])

#Calculate Long
gps['longtitude(deg)'] = ""
for i in range(0, len(gps['11611.8089317'])):
    gps['longtitude(deg)'][i] = float(gps['11611.8089317'][i].astype(str)[:3]) + (float(gps['11611.8089317'][i].astype(str)[3:])/60)


#calculate lat
gps['latitude(deg)'] = ""
for i in range(0, len(gps['4336.0259215'])):
    gps['latitude(deg)'][i] = float(gps['4336.0259215'][i].astype(str)[:2]) + (float(gps['4336.0259215'][i].astype(str)[2:])/60)


# x_min = min(longs_con)
# x_max = max(longs_con)
# y_min = min(lats_con)
# y_max = max(lats_con)
    
# fig, ax = plt.subplots(figsize=(16,8))
# im = ax.scatter(longs_con, lats_con, c=range(len(longs_con)))
# plt.axis([x_min, x_max, y_min, y_max])
# fig.colorbar(im, ax=ax)
# plt.axis([x_min, x_max, y_min, y_max])
    

x_min = min(gps['longtitude(deg)'])
x_max = max(gps['longtitude(deg)'])
y_min = min(gps['latitude(deg)'])
y_max = max(gps['latitude(deg)'])
fig, ax = plt.subplots(figsize=(16,8))
im = ax.scatter(gps['longtitude(deg)'], gps['latitude(deg)'], c=range(len(gps['longtitude(deg)'])))
plt.axis([x_min, x_max, y_min, y_max])
fig.colorbar(im, ax=ax)

def calc_distances(coords: pd.DataFrame,
                  col_lat='latitude(deg)',
                  col_lon='longtitude(deg)',
                  point_obj=Point) -> pd.DataFrame:
    traces = len(coords)
    distances = [None] * (traces)
    for i in range(traces):
        start = point_obj((coords.iloc[0][col_lat], coords.iloc[0][col_lon]))
        # Find the distance from the mean location
        #start = point_obj((coords[col_lat].mean(), coords[col_lon].mean()))
        finish = point_obj((coords.iloc[i][col_lat], coords.iloc[i][col_lon]))
        distances[i] = {
            'start': start,
            'finish': finish,
            'path distance': distance.geodesic(start, finish).meters,
        }
    
    distVec = pd.DataFrame(distances)["path distance"]

    return distances, distVec



distances, dists = calc_distances(gps)

pd.DataFrame(distances).plot(y='path distance', use_index=True, title =' distance from start')


















