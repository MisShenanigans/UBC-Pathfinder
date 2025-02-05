import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import math



# Read the csv file
df = pd.read_csv('data/ubcv_buildings_simple.csv')

# Create a graph
G = nx.Graph()

# Add nodes to the graph
for i in range(len(df)):
    G.add_node(df['BLDG_CODE'][i], pos=(-df['LONG'][i], -df['LAT'][i]))

# Add edges only to the three closest nodes
for i in range(len(df)):
    distances = []
    for j in range(len(df)):
        if i != j:
            distance = math.sqrt((df['LAT'][i] - df['LAT'][j])**2 + (df['LONG'][i] - df['LONG'][j])**2)
            distances.append((distance, df['BLDG_CODE'][j]))
    distances.sort()  # Sort by distance
    for _, neighbor in distances[:5]:
        G.add_edge(df['BLDG_CODE'][i], neighbor)

# Draw the graph
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True, node_size=50, font_size=8)

# Ensure equal aspect ratio
plt.axis('equal')

plt.title("Graph of UBC Buildings")
plt.show()