class Solution(object):
	def convertToTitle(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		retstr = ""
		while n > 0:
			cur = chr((n-1)%26+ord('A'))
			retstr = cur + retstr
			n = (n-1)/26
		return retstr
