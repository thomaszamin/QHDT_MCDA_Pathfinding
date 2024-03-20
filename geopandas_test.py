import pandas as pd
import geopandas
from shapely.geometry import Point
import matplotlib.pyplot as plt

# replace the path with your path
df = pd.read_csv('./QHDT_MCDA_Pathfinding/elevation_output/masspoint_new.csv')

geometry = [Point(xy) for xy in zip(df.iloc[:, 4], df.iloc[:, 5])]

gdf = geopandas.GeoDataFrame(df, geometry=geometry)

gdf.plot(column='z')

# replace the new file name with the old .csv's name
plt.savefig('masspoint_new.tiff')