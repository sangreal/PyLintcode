class Solution:
	# @param {int} n an integer
	# @return {int[][]} a square matrix
	def generateMatrix(self, n):
		retvec = [[0 for i in xrange(n)] for j in xrange(n)]

		rowupper, rowdown, colleft, colright = 0, n-1, 0, n-1

		curnum = 1
		while True:
			for i in xrange(colleft, colright+1):
				retvec[rowupper][i] = curnum
				curnum += 1
			rowupper += 1
			if rowupper > rowdown:
				break

			for j in xrange(rowupper, rowdown+1):
				retvec[j][colright] = curnum
				curnum += 1
			colright -= 1
			if colleft > colleft:
				break

			for t in xrange(colright, colleft-1, -1):
				retvec[rowdown][t] = curnum
				curnum += 1
			rowdown -= 1
			if rowupper > rowdown:
				break

			for k in xrange(rowdown, rowupper-1, -1):
				retvec[k][colleft] = curnum
				curnum += 1
			colleft += 1
			if colleft > colright:
				break

		return retvec