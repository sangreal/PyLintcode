import math
class Solution(object):
    def backtrack(self, n, idx, curvec, retveclist):
        if n == 1 and len(curvec) > 1:
            retveclist.append(curvec)
            return

        for i in xrange(idx, int(math.sqrt(n))+1):
            if n % i == 0:
                self.backtrack(n / i, i, curvec + [i], retveclist)
        if n > 1:
            self.backtrack(1, n, curvec + [n], retveclist)
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        retveclist = []
        self.backtrack(n, 2, [], retveclist)
        return retveclist
