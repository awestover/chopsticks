# a method that might not work for chopsticking

from anytree import Node, RenderTree
from anytree.exporter import DotExporter

import pdb

# functions that are used by every version and do not change
# these may have to be overriden / not used in very different versions of the game
# ie preservation
import random

# gameplay

# is the game over?
def gameOver(state, depth=0):
    p1 = ( state[0] == 0 and state[1] == 0 )
    p2 = ( state[2] == 0 and state[3] == 0 )
    if p1:
        return 1
    elif p2:
        return 2
    elif depth > 100:
        return 0
    else:
        return -1

# gets a move from moves that we know are good
def randomState(previousState, mod=5):
    return random.choice(possibleNextMoves(previousState, mod=mod))

# random state, does every possible hit and every possible switch not every possible state, only valid moves allowed
def possibleNextMoves(p, mod=5):
    lc = []  # probably legit hits, still pass it through validMove checker though
    # hits
    for i in range(0, 2):
        for j in range(2, 4):
            if p[i] != 0 and p[j] != 0: # 0 hit is not allowed
                cur = p[:]
                cur[j] = (cur[i] + cur[j]) % mod
                if conform(cur) not in lc:
                    lc.append(conform(cur))
    # switches
    # note these are already conformed
    cc = p[:]
    cc[1] = cc[0] + cc[1]
    cc[0] = 0
    while cc[1] >= cc[0]:
        if cc[1] < mod:
            if cc[0] != p[0]:  # can not be the same strategy you already have
                lc.append(cc[:])
        cc[0] += 1
        cc[1] -= 1
    return lc



# change hands format

# makes it so that all identical hand states are treated as the same
def conform(state):
    """
    new format is
    [ small big small big]
    without loss of generality
    """
    return [min(state[0], state[1]), max(state[0], state[1]), min(state[2], state[3]), max(state[2], state[3])]

# flips the reference frame
def invertState(state):
    return [state[2], state[3], state[0], state[1]]


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


mod = 3
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
DotExporter(root).to_picture("super_tree3.png")
