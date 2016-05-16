class Solution(object):
	def titleToNumber(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		
		ret = 0
		for i in xrange(len(s)):
			num = ord(s[i])- ord('A')+1
			ret = ret*26+num
		return ret

