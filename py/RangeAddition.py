class Solution(object):
	def getModifiedArray(self, length, updates):
		"""
    	:type length: int
    	:type updates: List[List[int]]
    	:rtype: List[int]
    	"""
		if length == 0 or len(updates) == 0 or len(updates[0]) == 0:
			return []

		strlist = [0 for i in xrange(length)]
		m, n = len(updates), 3
		for i in xrange(m):
			beginIdx, endIdx, inc = updates[i][0] , updates[i][1], updates[i][2]
			strlist[beginIdx] += inc
			if endIdx < m-1:
				strlist[endIdx+1] -= inc

		def partial_sum(iterable):
			partsum = 0
			for i in iterable:
				partsum += i
				yield partsum


		return list(partial_sum(strlist))
