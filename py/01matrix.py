import sys
class Solution(object):
    def updateMatrixdfs(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0:
            return None
        rows, cols = len(matrix), len(matrix[0])
        visited = [[sys.maxint for i in xrange(cols)] for j in xrange(rows)]
        for i in xrange(rows):
            for j in xrange(cols):
                if matrix[i][j] == 0:
                    visited[i][j] = 0

        def dfs(curx, cury):
            if curx < 0 or cury < 0 or curx > rows-1 or cury > cols-1:
                return sys.maxint
            if visited[curx][cury] != sys.maxint:
                return visited[curx][cury]
            if matrix[curx][cury] == 0:
                return 0

            for i, j in zip((1, 0, -1, 0), (0, 1, 0, -1)):
                ret = dfs(curx + i, cury + j)
                if ret != sys.maxint:
                    visited[curx][cury] = min(1 + ret, visited[curx][cury])
            return visited[curx][cury]

        for i in xrange(rows):
            for j in xrange(cols):
                if matrix[i][j] == 1:
                    dfs(i, j)
        return visited

    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0:
            return None

        rows, cols = len(matrix), len(matrix[0])
        ans = [[0 for i in xrange(cols)] for j in xrange(rows)]
        steps = 0
        queue = []
        for i in xrange(rows):
            for j in xrange(cols):
                if matrix[i][j] == 1:
                    queue.append((i, j))

        while queue:
            steps += 1
            mqueue, nqueue = [], []

            for x, y in queue:
                haszeros = False
                for i, j in zip((1, 0, -1, 0), (0, 1, 0, -1)):
                    curx, cury = x+i, y+j
                    if 0 <= curx < rows and 0 <= cury < cols and matrix[curx][cury] == 0:
                        haszeros = True
                        break
                if haszeros:
                    mqueue.append((x, y))
                    ans[x][y] = steps
                else:
                    nqueue.append((x, y))

            for x, y in mqueue:
                matrix[x][y] = 0
            queue = nqueue
        return ans


if __name__ == '__main__':
    s = Solution()
    matrix = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    retlist = s.updateMatrix(matrix)
    print retlist
