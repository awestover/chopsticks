# a method that might not work for chopsticking

from universal_functions import *
from anytree import Node, RenderTree
from anytree.exporter import DotExporter

import pdb

"""
conventions:
first listed hand is about to move (it is their turn)
left hand <= right hand
"""

def freeze(state):
	s = [str(sa) for sa in state]
	return "_".join(s)

def thaw(state):
	s = state.split("_")
	s = [int(se) for se in s]
	return s


# uses the anytree node class a lot, and extends it
class graphy_tree():
	# initialize the hybrid data structure
	def __init__(self, value, parent=None):
		if parent == None:
			self.node = Node(value)
		else:
			self.node = Node(value, parent=parent.node)
		self.parent = parent
		self.children = []

	# is the element anywhere in the tree? (recursive)
	def inTree(self, value):
		if self.node.name == value:
			return True
		for kid in self.children:
			return kid.inTree(value) 

	# add  a child to the children array and to the node
	def addChild(self, child):
		kid = graphy_tree(child, parent=self)
		self.children.append(kid)
		return kid

	# checks if something already has this ancestor
	def has_ancestor(self, ancestor):
		if self.parent != None:
			if self.parent.node.name == ancestor.node.name:
				return True
			elif self.parent.has_ancestor(ancestor):
				return True
		return False

	# counts all of the elements in the tree with no children
	def countLeaves(self):
		if len(self.children) != 0:
			ct = 0
			for kid in self.children:
				ct += kid.countLeaves()
			return ct
		else:
			return 1

	# makes sure an arrow would not be an EXACT copy
	def exact_exists(self, value):
		if value == "1_1_1_1":
			pdb.set_trace()
		for kid in self.node.children:
			if kid.name == value:
				return True
		return False

	# detect a duplicate parent
	def parent_exists(self):
		pass


mod = 4
rounds = 6

root = graphy_tree("1_1_1_1")
parents = [root]


def pTree(root):
	for pre, fill, node in RenderTree(root):
		print("%s%s" % (pre, node.name))

def next_gen(parents, gen):
	out = []
	for parent in parents:
		out.append([])
		cur_state = thaw(parent.node.name)

		if gen % 2 == 1:  # "enemy" move
			cur_state = invertState(cur_state)

		nexts = possibleNextMoves(cur_state, mod=mod)

		if gen % 2 == 1:  # "enemy" move
			nexts = [invertState(ne) for ne in nexts]	

		nexts = [freeze(ne) for ne in nexts]

		for ne in nexts:
			# if we REALLY already have it, do not even redraw it
			if not parent.exact_exists(ne):
				cur = parent.addChild(ne)  # at least have an arrow to it...
			# but it does not go to the next gen as a parent if it already happened in this branch of "fate"
			if not parent.has_ancestor(cur):
				out[-1].append(cur)
	return out



# def hasChildNamed(parent, child):
# 	if child == "1_1_1_2":
# 		print(parent, child, parent.children)
# 		pdb.set_trace()
# 	for kid in parent.children:
# 		if kid.name == child:
# 			return True
# 	return False
# 		# print(kid.name, child)

# all depths
for gen in range(0, rounds):
	kids = next_gen(parents, gen)

	parents = []
	for parent in kids:
		for kid in parent:
			parents.append(kid)

	ps = [p.node.name for p in parents]
	# print("\t\t\t".join(ps))
	print("Number of parents at generation {}  = \t {}".format(gen, len(ps)))
	print("\n")
	# pTree(root)


# print(hasChildNamed(root, ))
# import pdb
# pdb.set_trace()

# graphviz needs to be installed for the next line!
DotExporter(root.node).to_picture("tree.png")
