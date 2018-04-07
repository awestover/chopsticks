from anytree import Node, RenderTree
udo = Node("Udo")
marc = Node("Marc", parent=udo)
lian = Node("Lian", parent=marc)
dan = Node("Dan", parent=udo)
jet = Node("Jet", parent=dan)
jan = Node("Jan", parent=dan)
joe = Node("Joe", parent=dan)


# control H for find replace

def pTree(root):
	for pre, fill, node in RenderTree(root):
		print("%s%s" % (pre, node.name))

pTree(udo)

from anytree.exporter import DotExporter
# graphviz needs to be installed for the next line!
DotExporter(udo).to_picture("udo.png")

print(marc.children[0].name)