# a method that might not work for chopsticking

from universal_functions import *
from anytree import Node, RenderTree
from anytree.exporter import DotExporter

import pdb

"""
conventions:
first listed hand is about to move (it is their turn)
left hand <= right hand

I'm going to ENFORCE that you cannot have more than one of each node.
We will use a different data structure, simply a dictionary, and put it in a tree at the end

NEW CONVENTION
when you make a move it inverts the state after you go as part of the move
"""


def freeze(state):
	s = [str(sa) for sa in state]
	return "_".join(s)

def thaw(state):
	s = state.split("_")
	s = [int(se) for se in s]
	return s


mod = 5
rounds = 100

# parent: {children} is the format of the graph
graph = {"1_1_1_1":set()}
parents = ["1_1_1_1"]


def pTree(root):
	for pre, fill, node in RenderTree(root):
		print("%s%s" % (pre, node.name))

def next_gen(parents):
	out = {}
	for parent in parents:
		out[parent] = set()

		cur_state = thaw(parent)
		nexts = possibleNextMoves(cur_state, mod=mod)
		nexts = [invertState(ne) for ne in nexts]
		nexts = [freeze(ne) for ne in nexts]

		for ne in nexts:
			out[parent].add(ne)

	return out

# all depths
for gen in range(0, rounds):
	kids = next_gen(parents)
	nextParents = []
	for parent in parents:
		if graph.get(parent) == None:
			graph[parent] = set()

		for kid in kids[parent]:
			if kid not in graph[parent]:
				graph[parent].add(kid)
				nextParents.append(kid)

	print("Number of parents at generation {}  = \t {}\n".format(gen, len(parents)))
	parents = nextParents


print("turn it into a tree")


root = Node("1_1_1_1")

prevGen = [root]
while prevGen != []:
	nextGen = []
	for parent in prevGen:
		children = graph[parent.name]
		for child in children:
			nextGen.append(Node(child, parent=parent))
		graph[parent.name] = []
	prevGen = nextGen

print("Exporting to a picture")

def pTree(root):
	for pre, fill, node in RenderTree(root):
		print("%s%s" % (pre, node.name))

pdb.set_trace()
# graphviz needs to be installed for the next line!
DotExporter(root).to_picture("super_tree.png")
