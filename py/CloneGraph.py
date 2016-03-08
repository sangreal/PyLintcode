import collections

# Definition for a undirected graph node
class UndirectedGraphNode(object):
	def __init__(self, x):
		self.label = x
		self.neighbors = []

class Solution(object):
	def serialize(self, node):
		if node == None:
			return ""

		neiborset = collections.defaultdict(set)
		nodevec = collections.deque()
		nodevec.append(node)

		retStr = ""

		while len(nodevec) > 0:
			curnode = nodevec.popleft()
			retStr += str(curnode.label)
			retStr += ','
			for neib in curnode.neighbors:
				nlabel = neib.label
				if nlabel not in neiborset[curnode.label]:
					neiborset[curnode.label].add(nlabel)
					retStr += str(nlabel)
					retStr += ','
				if curnode.label not in neiborset[nlabel]:
					neiborset[nlabel].add(curnode.label)
			retStr = retStr[0:len(retStr)-1]
			retStr += '#'
		return retStr

	def deserialize(self, nodestr):
		if len(nodestr) == 0:
			return None

		strlist = nodestr.split('#')
		hlabel = strlist[0]
		headNode = UndirectedGraphNode(hlabel)
		nodemap = collections.defaultdict()
		nodemap[hlabel] = headNode

		for periodstr in strlist:
			nodelist = periodstr.split(',')
			rootNode = None
			for i in xrange(len(nodelist)):
				nlabel = nodelist[i]
				if nlabel not in nodemap:
					newnode = UndirectedGraphNode(int(nlabel))
					nodemap[nlabel] = newnode

				if i == 0:
					rootNode = nodemap[nlabel]
				if i > 0:
					rootNode.neighbors.append(nodemap[nlabel])
					nodemap[nlabel].append(rootNode)
		return headNode


	def cloneGraph(self, node):
		"""
		:type node: UndirectedGraphNode
		:rtype: UndirectedGraphNode
		"""
		retNode = self.deserialize(self.serialize(node))
		return retNode