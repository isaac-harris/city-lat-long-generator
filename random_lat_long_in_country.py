# # imports
# import re
# import random
# import shapefile
# from shapely.geometry import shape, Point

# # function that takes a shapefile location and a country name as inputs
# def random_point_in_country(shp_location, country_name):
#     shapes = shapefile.Reader(shp_location) # reading shapefile with pyshp library
#     country = [s for s in shapes.records() if country_name in s][0] # getting feature(s) that match the country name 
#     country_id = int(re.findall(r'd+', str(country))[0]) # getting feature(s)'s id of that match

#     shapeRecs = shapes.shapeRecords()
#     feature = shapeRecs[country_id].shape.__geo_interface__

#     shp_geom = shape(feature)

#     minx, miny, maxx, maxy = shp_geom.bounds
#     while True:
#         p = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
#         if shp_geom.contains(p):
#             return p.x, p.y

# random_point_in_country("TM_WORLD_BORDERS-0.3.dbf", "Ukraine")

from itertools import count
from matplotlib.pyplot import get
from sqlalchemy import over
import geopandas as gpd
import numpy as np

def get_country_points(country_name = "GBR", num_samples = 10):
  overall_polys = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
  gdf_polys = overall_polys[overall_polys.iso_a3 == country_name]
  print(gdf_polys)

  x_min, y_min, x_max, y_max = gdf_polys.total_bounds

  x = np.random.uniform(x_min, x_max, num_samples)
  y = np.random.uniform(y_min, y_max, num_samples)

  gdf_points = gpd.GeoSeries(gpd.points_from_xy(x, y))

  gdf_points = gdf_points[gdf_points.within(gdf_polys.unary_union)]

  print(gdf_points)
  print(type(gdf_points))

get_country_points(country_name="GBR", num_samples=60)
get_country_points(country_name="ESP", num_samples=60)
get_country_points(country_name="CHE", num_samples=60)
get_country_points(country_name="BEL", num_samples=60)
get_country_points(country_name="DEU", num_samples=60)
get_country_points(country_name="SWE", num_samples=60)
get_country_points(country_name="USA", num_samples=60)
get_country_points(country_name="PSE", num_samples=60)

# overall_polys = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# print(overall_polys[overall_polys.name == "France"])

get_city_points()