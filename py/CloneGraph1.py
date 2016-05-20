# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
	def cloneGraph(self, node):
		"""
		:type node: UndirectedGraphNode
		:rtype: UndirectedGraphNode
		"""
		if node is None:
			return None

		cloneroot = UndirectedGraphNode(node.label)
		stack = [node]
		store = {node.label:cloneroot}

		while len(stack) > 0:
			curnode = stack.pop()
			clonenode = store[curnode.label]
			for neibor in curnode.neighbors:
				if neibor.label not in store:
					newnode = UndirectedGraphNode(neibor.label)
					store[neibor.label] = newnode
					stack.append(neibor)

				clonenode.neighbors.append(store[neibor.label])

		return cloneroot