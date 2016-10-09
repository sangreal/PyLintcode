class Solution(object):
    def dfsHelper(self, base, n, retlist):
        for i in xrange(10):
            curnum = base*10 + i
            if curnum <= n:
                retlist.append(curnum)
                self.dfsHelper(curnum, n, retlist)
            else:
                break

    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        retlist = []
        for i in xrange(1, 10):
            if i <= n:
                retlist.append(i)
                self.dfsHelper(i, n , retlist)
        return retlist
