class Solution(object):
	def validWordSquare(self, words):
		"""
		:type words: List[str]
		:rtype: bool
		"""
		idx = 0
		if len(words) == 0:
			return True
		rowcnt, colcnt = len(words), len(words[0])
		if rowcnt != colcnt:
			return False

		for idx in xrange(rowcnt):
			colcnt = len(words[idx])

			xlen = 0

			for n in xrange(rowcnt):
				if len(words[n]) < idx+1:
					break
				xlen += 1
			if xlen != colcnt:
				return False

			for i in xrange(colcnt):
				if words[idx][i] != words[i][idx]:
					return False
		return True