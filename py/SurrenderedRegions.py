import collections

class Solution(object):
	def bfs(self, board, row, col, visited):
		toFlip = []
		touchWall = False

		height, width = len(board), len(board[0])
		bfsStore = collections.deque([(row, col)])
		def getNextNode(i, j):
			if i > 0 and board[i-1][j] == 'O' and visited[i-1][j] == 0: bfsStore.append((i-1, j))
			if i < height-1 and board[i+1][j] == 'O' and visited[i+1][j] == 0: bfsStore.append((i+1, j))
			if j > 0 and board[i][j-1] == 'O' and visited[i][j-1] == 0: bfsStore.append((i, j-1))
			if j < width-1 and board[i][j+1] == 'O' and visited[i][j+1] == 0: bfsStore.append((i, j+1))

		while len(bfsStore) > 0:
			tmprow, tmpcol = bfsStore.popleft()
			if tmprow == 0 or tmprow == height-1 or tmpcol == 0 or tmpcol == width-1:
				touchWall = True

			if visited[tmprow][tmpcol] == 0:
				visited[tmprow][tmpcol] = 1
				toFlip.append((tmprow, tmpcol))
				getNextNode(tmprow, tmpcol)

		if touchWall == False:
			for x, y in toFlip:
				board[x][y] = 'X'
	def solve(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		if len(board) == 0 or len(board[0]) == 0:
			return

		height, width = len(board), len(board[0])

		visited = [[0 for i in xrange(width)] for j in xrange(height)]
		for i in xrange(height):
			for j in xrange(width):
				if visited[i][j] == 0 and board[i][j] == 'O':
					self.bfs(board, i, j, visited)
