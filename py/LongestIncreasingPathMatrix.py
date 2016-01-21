class Solution(object):
    def dfs(self, matrix, i, j, rowcount, colcount, stormap):
        if i < 0 or j < 0 or i >= rowcount-1 or j >= colcount-1:
            return 0
        if stormap[i][j] > 0:
            return self.stormap[i][j]

        if matrix[i][j] < matrix[i-1][j]:
            stormap[i][j] = max(stormap[i][j], self.dfs(matrix, i-1, j, rowcount, colcount, stormap))
        if matrix[i][j] < matrix[i+1][j]:
            stormap[i][j] = max(stormap[i][j], self.dfs(matrix, i+1, j, rowcount, colcount, stormap))
        if matrix[i][j] < matrix[i][j-1]:
            stormap[i][j] = max(stormap[i][j], self.dfs(matrix, i, j-1, rowcount, colcount, stormap))
        if matrix[i][j] < matrix[i][j+1]:
            stormap[i][j] = max(stormap[i][j], self.dfs(matrix, i, j+1, rowcount, colcount, stormap))

        stormap[i][j] += 1
        return stormap[i][j]

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        rowcount, colcount = len(matrix), len(matrix[0])
        stormap = [[0 for x in xrange(colcount)] for x in xrange(rowcount)]

        maxlen = 0

        for i in xrange(rowcount):
            for j in xrange(colcount):
                maxlen = max(maxlen, self.dfs(matrix, i, j, rowcount, colcount, stormap))

        return maxlen
