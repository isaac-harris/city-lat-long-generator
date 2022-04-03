from cmath import sin
from itertools import count
from matplotlib.pyplot import get
from sqlalchemy import over
import geopandas as gpd
import numpy as np
import pandas as pd
import random
from cmath import sin
from cmath import cos
from math import sqrt


pi = 3.141593
# https://www.johndcook.com/how_big_is_a_degree.html
# ^ find out your long_to_km value by inputting the latitude if the location into this

def city_dataset(lat,long,area,number,long_to_km):
    """
    this calculates random lat long coordinates based on: 
        the coordinates of the centre of the region 
        the approximate area of that region
        the number of desired samples
        the conversion between 1 degree change in longitude at a certain latitude (use website above to find this, 
            for example closer to the poles a change in longitude by a degree results in a smaller change in kilometres than at the equator)
    we assume a generally circular region.

    """
    area_angle_radius = []
    area_lat_long = []
    lat_to_km = 111

    radius_974 = 0.974 * sqrt((area/pi))

    for i in range(0,number):
        area_angle_radius += [[np.random.uniform(0, 2*pi),np.random.uniform(0,radius_974)]]

        area_lat_long += [[(lat+sin(area_angle_radius[i][0])*area_angle_radius[i][1]*(1/lat_to_km)).real, (long+cos(area_angle_radius[i][0])*area_angle_radius[i][1]*(1/long_to_km)).real]]

    print(area_lat_long)


malaga_lat_long_dataset = city_dataset(36.732122,-4.428117,398,500,89)
seville_lat_long_dataset = city_dataset(37.289091,-5.984459,140,210,88)
tangier_lat_long_dataset = city_dataset(35.754989,-5.833954,116,280,90)