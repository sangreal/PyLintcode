import collections
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        pres = [-1] * N * N
        for i in xrange(N * N):
            pres[i] = i

        def find(val):
            while pres[val] != val:
                val = pres[val]
            return val
        def union(val1, val2):
            n1, n2 = find(val1), find(val2)
            if n1 < n2:
                pres[n2] = n1
            else:
                pres[n1] = n2
            return min(n1, n2)

        storemap = collections.defaultdict(int)
        for i in xrange(N):
            for j in xrange(N):
                if M[i][j] == 1:
                    if i > 0 and M[i-1][j] == 1:
                        idx = union(i, i-N)
                        storemap[idx] += 1
                    if j > 0 and M[i][j-1] == 1:
                        idx = union(i, i-1)
                        storemap[idx] += 1

        ans = 0
        for v in storemap.itervalues():
            if v > 0:
                ans += 1
        return ans
