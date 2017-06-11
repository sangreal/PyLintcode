class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        def nearBombcnt(board, x, y):
            bomb = 0
            rows, cols = len(board), len(board[0])
            if x > 0 and y > 0:
                if board[x-1][y-1] == 'M':
                    bomb += 1
            if x > 0:
                if board[x-1][y] == 'M':
                    bomb += 1
            if y > 0:
                if board[x][y-1] == 'M':
                    bomb += 1
            if x < rows-1 and y < cols-1:
                if board[x+1][y+1] == 'M':
                    bomb += 1
            if x < rows-1:
                if board[x+1][y] == 'M':
                    bomb += 1
            if y < cols-1:
                if board[x][y+1] == 'M':
                    bomb += 1
            if x > 0 and y < cols-1:
                if board[x-1][y+1] == 'M':
                    bomb += 1
            if x < rows-1 and y > 0:
                if board[x+1][y-1] == 'M':
                    bomb += 1
            return bomb

        def getEmptyList(board, x, y, visited):
            rows, cols = len(board), len(board[0])
            retlist = []
            if x > 0:
                if board[x-1][y] == 'E' and visited[x-1][y] == 0:
                    print 'x-1  %d %d' %(x-1, y)
                    retlist.append((x-1, y))
            if y > 0:
                if board[x][y-1] == 'E' and visited[x][y-1] == 0:
                    retlist.append((x, y-1))
            if x < rows-1:
                if board[x+1][y] == 'E' and visited[x+1][y] == 0:
                    retlist.append((x+1, y))
            if y < cols-1:
                if board[x][y+1] == 'E' and visited[x][y+1] == 0:
                    retlist.append((x, y+1))
            return retlist
        def isBomb(x, y):
            return True if board[x][y] == 'X' else False
        if len(board) == 0:
            return None
        rows, cols = len(board), len(board[0])
        visited = [[0 for i in xrange(cols)] for j in xrange(rows)]

        cx, cy = click[0], click[1]
        if board[cx][cy] == 'M':
            board[cx][cy] = 'X'
            return board

        queue = [(cx, cy)]
        while queue:
            nqueue = []
            while queue:
                x, y = queue.pop(0)
                visited[x][y] = 1
                bombcnt = nearBombcnt(board, x, y)
                if x == 1 and y == 0:
                    print 'bomcnt : %d' %(bombcnt)
                if bombcnt > 0:
                    board[x][y] = str(bombcnt)
                else:
                    board[x][y] = 'B'

                    nqueue.extend(getEmptyList(board, x, y, visited))
            queue = nqueue
        return board

if __name__ == "__main__":
    s = Solution();
    board = [['E','E','E','E','E'],['E','E','M','E','E'],['E','E','E','E','E'],['E','E','E','E','E']]
    click = [3, 0]
    s.updateBoard(board, click)
