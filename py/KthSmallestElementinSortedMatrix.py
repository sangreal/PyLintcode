class Solution(object):
	def quickselect(self, matrix, k):
		rowcnt, colcnt = len(matrix), len(matrix[0])
		lens = rowcnt*colcnt
		pivot = matrix[lens/k][lens%k]
		lstr, rstr = [], []
		for i in xrange(rowcnt):
			for j in xrange(colcnt):
				if matrix[i][j] < pivot:
					lstr.append(matrix[i][j])
				elif matrix[i][j] > pivot:
					rstr.append(matrix[i][j])

		if len(lstr) >= k:
			return self.quickselect(matrix, k)
		elif k > lens - len(rstr):
			return self.quickselect(matrix, k-(lens-len(rstr)))
		else:
			return pivot

	def kthSmallest(self, matrix, k):
		"""
		:type matrix: List[List[int]]
		:type k: int
		:rtype: int
		"""
		return self.quickselect(matrix, k)
