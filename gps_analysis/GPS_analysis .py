#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 16:34:47 2022

@author: tamalaku
"""
import pandas as pd
import matplotlib.pyplot as plt
from geopy import Point, distance

import pandas as pd
  
# url = "/Users/tamalaku/Documents/skydar/GPS_data_6_29.csv"
# df = pd.read_csv(url)
# df = df.iloc[114:]
# print(df)


gps= pd.read_csv("/Users/tamalaku/Documents/skydar/data_7_7.csv",lineterminator='\n')
gps.drop(gps[gps['time'] == "time"].index, inplace = True)
# gps=df
gps['Time'] = pd.to_datetime(gps['time'],format='%H%M%S') - pd.Timedelta(hours=6) - pd.Timedelta(seconds=18)
# gps['Time'] = gps['Date'].dt.strftime("%H:%M:%S").str.replace(':','')
gps['Time'] = gps['Time'].dt.time



#calculate lat
gps['latitude(deg)'] = ""
for i in range(0, len(gps['latitude'])):
    gps['latitude(deg)'][i] = float(gps['latitude'][i].astype(str)[:2]) + (float(gps['latitude'][i].astype(str)[2:])/60)


#Calculate Long
gps['longitude(deg)'] = ""
for i in range(0, len(gps['longitude'])):
    gps['longitude(deg)'][i] = float(gps['longitude'][i].astype(str)[:3]) + (float(gps['longitude'][i].astype(str)[3:])/60)


x_min = min(gps['longitude(deg)'])
x_max = max(gps['longitude(deg)'])
y_min = min(gps['latitude(deg)'])
y_max = max(gps['latitude(deg)'])
fig, ax = plt.subplots(figsize=(16,8))
im = ax.scatter(gps['longitude(deg)'], gps['latitude(deg)'], c=range(len(gps['longitude(deg)'])))

# im = ax.scatter(gps['longitude(deg)'][400:600], gps['latitude(deg)'][400:600], c=range(len(gps['longitude(deg)'][400:600])))
plt.axis([x_min, x_max, y_min, y_max])
fig.colorbar(im, ax=ax)



def calc_distances(coords: pd.DataFrame,
                  col_lat='latitude(deg)',
                  col_lon='longitude(deg)',
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








# gps.drop(gps[gps['time'] == "time"].index, inplace = True)










