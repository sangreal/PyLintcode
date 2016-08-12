import collections

class Solution(object):
    def find(self, m, parents):
        i = m
        while parents[i] != i:
            i = parents[i]
        return i

    def union(self, m, n, parents, sizes, counts):
        mroot = self.find(m, parents)
        nroot = self.find(n, parents)
        if mroot == nroot:
            return counts

        if (sizes[mroot] < sizes[nroot]):
            parents[mroot] = nroot
            sizes[nroot] += sizes[mroot]
        else:
            parents[nroot] = mroot
            sizes[mroot] += sizes[nroot]
        return counts-1

    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parents = [0] * n
        sizes = [1] * n
        for i in xrange(n):
            parents[i] = i

        counts = n
        for i in xrange(len(edges)):
            m, n = edges[i][0], edges[i][1]
            counts = self.union(m, n, parents, sizes, counts)

        return counts
