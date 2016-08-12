# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def getInteger(self):
       """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution(object):
	def depthSearch(self, nestInt, depth):
		if nestInt.isInteger():
			return nestInt.getInteger()*depth
		retval = 0
		nestlist = nestInt.getList()
		for nest in nestlist:
			retval += self.depthSearch(nest, depth+1)
		return retval

	def depthSum(self, nestedList):
		"""
		:type nestedList: List[NestedInteger]
		:rtype: int
		"""
		retsum = 0
		for item in nestedList:
			retsum += self.depthSearch(item, 1)
		return retsum
