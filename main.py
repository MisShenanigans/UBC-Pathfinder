import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import math

# Read the csv file
df = pd.read_csv('ubcv_buildings_simple.csv')

# Create a graph
G = nx.Graph()

# Add nodes to the graph
for i in range(len(df)):
    G.add_node(i, pos=(df['LONG'][i], df['LAT'][i]))

# Add edges only to the three closest nodes
for i in range(len(df)):
    distances = []
    for j in range(len(df)):
        if i != j:
            distance = math.sqrt((df['LAT'][i] - df['LAT'][j]) ** 2 + (df['LONG'][i] - df['LONG'][j]) ** 2)
            distances.append((distance, j))
    distances.sort()  # Sort by distance
    for _, neighbor in distances[:3]:
        G.add_edge(i, neighbor)

# Draw the graph without labels
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=False, node_size=50)

print("Plotting")
plt.show()
