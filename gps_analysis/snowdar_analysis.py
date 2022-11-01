#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:23:13 2022

@author: tamalaku
"""
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


lidar= pd.read_csv("/Users/tamalaku/Documents/skydar/SNODAR-C5BA8EF761C6__07JUL2022-1100_THRU_07JUL2022-1200.csv",lineterminator='\n')
lidar.drop(lidar[lidar['DATE'] == "DATE"].index, inplace = True)
lidar['Date'] = pd.to_datetime(lidar['DATE'])
lidar['Time'] = lidar['Date'].dt.time

