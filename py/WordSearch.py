class Solution(object):
    def wordSearch(self, board, word, pos, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == '.':
            return False
        if board[i][j] != word[pos]:
            return False
        elif board[i][j] == word[pos] and pos == len(word)-1:
            return True

        tmp, board[i][j] = board[i][j], :'.'
        ret1 = self.wordSearch(board, word, pos+1, i-1, j)
        if ret1 == True:
            return True
        ret2 = self.wordSearch(board, word, pos+1, i+1, j)
        if ret2 == True:
            return True
        ret3 = self.wordSearch(board, word, pos+1, i, j-1)
        if ret3 == True:
            return True
        ret4 = self.wordSearch(board, word, pos+1, i, j+1)
        if ret4 == True:
            return True

        board[i][j] = tmp
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if len(board) == 0 or len(board[0]) == 0:
            return False

        rowlen = len(board)
        colen = len(board[0])

        for i in xrange(0, rowlen):
            for j in xrange(0, colen):
                if self.wordSearch(board, word, 0, i, j):
                        return True
        return False
