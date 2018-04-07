# import matplotlib.pyplot as plt
# import networkx as nx

# G = nx.cubical_graph()
# pos = nx.spring_layout(G) # positions for all nodes

# # nodes
# nx.draw_networkx_nodes(G,pos,nodelist=[0,1,2,3])
# nx.draw_networkx_nodes(G,pos,nodelist=[4,5,6,7])

# # edges
# nx.draw_networkx_edges(G,pos,width=1.0)
# nx.draw_networkx_edges(G,pos,edgelist=[(0,1),(1,2),(2,3),(3,0)])
# nx.draw_networkx_edges(G,pos,edgelist=[(4,5),(5,6),(6,7),(7,4)])

# # labels
# labels={0:"a", 1:"b", 2:"c", 3:"a", 4:"b", 5:"c", 6:"a", 7:"b"}
# nx.draw_networkx_labels(G,pos,labels,font_size=16)

# plt.axis('off')
# plt.savefig("labels_and_colors.png")
# plt.pause(1)


import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
# pos = nx.spring_layout(G) # positions for all nodes

# nodes
nx.draw_networkx_nodes(G,nodelist=[0,1,2,3])
nx.draw_networkx_nodes(G,nodelist=[4,5,6,7])

# edges
nx.draw_networkx_edges(G,width=1.0)
nx.draw_networkx_edges(G,edgelist=[(0,1),(1,2),(2,3),(3,0)])
nx.draw_networkx_edges(G,edgelist=[(4,5),(5,6),(6,7),(7,4)])

# labels
labels={0:"a", 1:"b", 2:"c", 3:"a", 4:"b", 5:"c", 6:"a", 7:"b"}
nx.draw_networkx_labels(G,labels,font_size=16)

plt.axis('off')
plt.savefig("labels_and_colors.png")
plt.pause(1)