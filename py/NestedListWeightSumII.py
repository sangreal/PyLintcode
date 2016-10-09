import collections

class NestedInteger(object):
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
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
    def constructVec(self, nestedList, l, storeVec):
        if len(nestedList) == 0:
            return

        for i in xrange(len(nestedList)):
            if nestedList[i].isInteger():
                storeVec[l].append(nestedList[i].getInteger())
            else:
                self.constructVec(nestedList[i], l+1, storeVec)

    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        storeVec = collections.defaultdict(list)
        self.constructVec(nestedList, 0, storeVec)
        rownum = len(storeVec)

        retsum = 0
        for i in xrange(rownum):
            colnum = len(storeVec[i])
            for j in xrange(colnum):
                retsum += (rownum-i)*storeVec[i][j]
        return retsum
