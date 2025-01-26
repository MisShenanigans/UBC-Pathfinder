# create a graph using the ubcv_buildings_simple.csv file, use LAT and LONG in the file to create the graph
# and then use the graph to find the shortest path between two buildings

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import heapq
import geopandas as gpd

# read the csv file
df = pd.read_csv('data/ubcv_roads_simple.geojson')

print(df.head())