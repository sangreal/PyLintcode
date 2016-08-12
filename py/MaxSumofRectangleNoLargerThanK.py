import bisect

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), 0
        if m > 0:
            n = len(matrix[0])

        M, N = max(m,n), min(m,n)
        ans = 0

        for x in xrange(N):
            sums = [0] * M
            for y in xrange(x, N):

                store, num = [], 0
                for z in xrange(M):
                    sums[z] += matrix[z][y] if m > n else matrix[y][z]
                    num += sums[z]
                    if (num <= k): ans = max(ans, num)

                    else:
                        i = bisect.bisect_left(store, num-k)
                        if i != len(store):
                            ans = max(ans, num-store[i])
                    bisect.insort(store,num)

        return ans
