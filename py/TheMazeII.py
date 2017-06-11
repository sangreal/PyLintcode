import sys
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if len(maze) == 0:
            return -1
        rows, cols = len(maze), len(maze[0])
        visited = [[0 for i in xrange(cols)] for j in xrange(rows)]
        Solution.shortestDistance.minpath = sys.maxint
        def dfs(st, dest, curcnt):
            x, y = st[0], st[1]
            if x < 0 or y < 0 or x > rows-1 or y > cols-1:
                return
            if x == dest[0] and y == dest[1]:
                 Solution.shortestDistance.minpath = min(curcnt,  Solution.shortestDistance.minpath)
                return

            visited[x][y] = 1
            tmpx, tmpy = x, y
            while tmpx > 0 and maze[tmpx-1][y] != 1:
                tmpx -= 1

            if visited[tmpx][y] == 0:
                dfs([tmpx, y], dest, curcnt+1)
            tmpx = x
            while tmpx <rows - 1 and maze[tmpx+1][y] != 1:
                tmpx += 1

            if visited[tmpx][y] == 0:
                dfs([tmpx, y], dest, curcnt+1)

            while tmpy > 0 and maze[x][tmpy-1] != 1:
                tmpy -= 1

            if visited[x][tmpy] == 0:
                dfs([x, tmpy], dest, curcnt+1)
            tmpy = y

            while tmpy < cols-1 and maze[x][tmpy+1] != 1:
                tmpy += 1
            if visited[x][tmpy] == 0:
                dfs([x, tmpy], dest, curcnt+1)
            return
        dfs(start, destination, 0)
        return minpath
