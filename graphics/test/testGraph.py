# import matplotlib.pyplot as plt
# import networkx as nx

# G=nx.Graph()

# # adding a list of edges
# G.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])

# nx.draw(G)
# plt.savefig("simple_path.png")
# plt.show()
import networkx as nx
import matplotlib.pyplot as plt

G=nx.path_graph(4)
cities = {0:"Toronto",1:"London",2:"Berlin",3:"New York"}

H=nx.relabel_nodes(G,cities)
 
print("Nodes of graph: ")
print(H.nodes())
print("Edges of graph: ")
print(H.edges())
nx.draw(H)
plt.savefig("path_graph_cities.png")
plt.show()