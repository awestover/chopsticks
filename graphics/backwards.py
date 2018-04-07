# a method that might not work for chopsticking

from universal_functions import *
import pdb

# inverted the graph, now people keep track of their parents, not their kids

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

# child: {parents} is the format of the graph
graph = {}
children = []
for ps in possibleNextMoves([1,1,1,1], mod=mod):
	children.append(freeze(ps))
	graph[children[-1]] = {"1_1_1_1"}

def next_gen(children):
	out = {}
	for child in children:
		cur_state = thaw(child)
		for ps in possibleNextMoves(cur_state, mod=mod):
			try:
				out[freeze(invertState(ps))].add(freeze(cur_state))
			except KeyError:
				out[freeze(invertState(ps))] = {freeze(cur_state)}
	return out

# fill the graph
gen = 0
while len(children) > 0:
	gen += 1
	kids = next_gen(children)
	nextChildren = []

	for child in kids:
		if graph.get(child) == None:
			graph[child] = set()
		for parent in kids[child]:
			added = False
			if parent not in graph[child]:
				added = True
				graph[child].add(parent)
			if added:
				nextChildren.append(child)

	print("Number of parents at generation {}  = \t {}\n".format(gen, len(children)))
	children = nextChildren


advisor = {}
gameOverStates = set()

for child in graph:
	if gameOver(thaw(child)) != -1:
		advisor[child] = 1
		gameOverStates.add(child)
	else:
		advisor[child] = 0

for goState in gameOverStates:
	# pdb.set_trace()
	kids = {goState}
	generation = 0
	while len(kids) > 0:
		generation += 1
		nextGen = set()
		for kid in kids:
			for parent in graph[kid]:
				if advisor[parent] != advisor[kid]:
					advisor[parent] = max(advisor[kid], advisor[parent]) 
					nextGen.add(parent)
		kids = nextGen

pdb.set_trace()