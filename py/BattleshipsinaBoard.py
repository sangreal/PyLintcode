class Solution(object):
    def countHelper(self, board, visited, i, j):
        if visited[i][j] == 1:
            return 0

        hasExtend = False
        rowcnt, colcnt = len(board), len(board[0])

        if (i > 0 and visited[i-1][j] == 1) or (j > 0 and visited[i][j-1] == 1):
            return 0

        while j < colcnt-1 and board[i][j+1] == 'X' and visited[i][j+1] == 0:
            hasExtend = True
            j += 1
            visited[i][j+1] = 1

        while i < rowcnt-1 and visited[i+1][j] == 0 and board[i+1][j] == 'X' and hasExtend == False:
            hasExtend = True
            i += 1
            visited[i+1][j] = 1

        return 1

    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if len(board) == 0:
            return 0

        rowcnt, colcnt = len(board), len(board[0])

        retcnt = 0
        for i in xrange(rowcnt):
            for j in xrange(colcnt):
                if board[i][j] == '.' or (i > 0 and board[i-1][j] == 'X') or (j > 0 and board[i][j-1] == 'X'):
                    continue
                retcnt += 1

        return retcnt
