# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
	def isInteger(self):
		"""
       @return {boolean} True if this NestedInteger holds a single integer,
       rather than a nested list.
       """
#
   def getInteger(self):
       """
       @return {int} the single integer that this NestedInteger holds,
       if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """
#
   def getList(self):
       """
       @return {NestedInteger[]} the nested list that this NestedInteger holds,
       if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator(object):

	def __init__(self, nestedList):
		self.idx = 0
		self.flatlist = []
		self.dfs(nestedList)
		self.listlen = len(self.flatlist)

	def dfs(self, inputlist):
		for node in inputlist:
			if node.getInteger():
				self.flatlist.append(node.getInteger())
			else:
				self.dfs(node.getList())


	def next(self):
		retNum = self.flatlist[self.idx]
		self.idx += 1
		return retNum


    # @return {boolean} true if the iteration has more element or false
	def hasNext(self):
		return self.idx < self.listlen


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())