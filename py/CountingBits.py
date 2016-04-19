class Solution(object):
	def countBits(self, num):
		"""
		:type num: int
		:rtype: List[int]
		"""
		retlist = [0 for i in xrange(num)]
		pow2, before = 1, 0

		for i in xrange(1, num+1):
			if i == pow2:
				before = 1
				retlist[i] = before
				pow2 <<= 1
			else:
				curnum = retlist[before] + 1
				before += 1

		return retlist