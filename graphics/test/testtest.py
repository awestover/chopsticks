# https://stackoverflow.com/questions/28533111/plotting-networkx-graph-with-node-labels-defaulting-to-node-name
import matplotlib.pyplot as plt
import networkx as nx

edgelist=[("1_1","2"),("3","4"),("4","1_1")]
H = nx.Graph(edgelist)

nx.draw(H, with_labels=True)
plt.pause(10)
