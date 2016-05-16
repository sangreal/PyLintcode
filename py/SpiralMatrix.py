class Solution(object):
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""

		m = len(matrix)
		if m == 0:
			return []
		n = len(matrix[0])
		if n == 0:
			return []

		retList = []
		rowleft, rowright = 0 , n-1
		colupper, coldown = 0, m-1

		while rowleft <= rowright and colupper <= coldown:
			for i in xrange(rowleft, rowright+1):
				retList.append(matrix[colupper][i])
			colupper += 1
			if colupper > coldown: break

			for j in xrange(colupper, coldown+1):
				retList.append(matrix[j][rowright])
			rowright -= 1
			if rowright < rowleft: break

			for k in xrange(rowright, rowleft-1, -1):
				retList.append(matrix[coldown][k])
			coldown -= 1
			if coldown < colupper: break
			
			for t in xrange(coldown, colupper-1, -1):
				retList.append(matrix[t][rowleft])
			rowleft += 1

		return retList