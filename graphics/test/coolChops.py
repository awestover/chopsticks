# a method that might not work for chopsticking

from universal_functions import *

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




# probably look for all win paths, but weight the shorter ones heavier and avoid loops...
# def winPaths(state):
# 	while not gameOver(state):


