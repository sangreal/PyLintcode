import collections

class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        if len(maze) == 0:
            return False

        rows, cols = len(maze), len(maze[0])
        queue = [start]
        visited = [[0 for i in xrange(cols)] for j in xrange(rows)]

        while queue:
            nqueue = []
            while queue:
                curlist = queue.pop(0)

                x, y = curlist[0], curlist[1]
                visited[x][y] = 1
                if x == destination[0] and y == destination[1]:
                    return True

                tmpx, tmpy = x, y
                while tmpx > 0 and maze[tmpx-1][y] != 1:
                    tmpx -= 1

                if visited[tmpx][y] == 0:
                    nqueue.append([tmpx, y])
                tmpx = x
                while tmpx <rows - 1 and maze[tmpx+1][y] != 1:
                    tmpx += 1

                if visited[tmpx][y] == 0:
                    nqueue.append([tmpx, y])

                while tmpy > 0 and maze[x][tmpy-1] != 1:
                    tmpy -= 1

                if visited[x][tmpy] == 0:
                    nqueue.append([x, tmpy])
                tmpy = y

                while tmpy < cols-1 and maze[x][tmpy+1] != 1:
                    tmpy += 1

                if visited[x][tmpy] == 0:
                    nqueue.append([x, tmpy])
            queue = nqueue
        return False

if __name__ == "__main__":
    s = Solution()
    maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    start = [0, 4]
    destination = [4, 4]
    s.hasPath(maze, start, destination)
