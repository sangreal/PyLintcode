class Solution(object):
	def longestValidParentheses(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		vec = []
		maxlen, accumlen, localmax = 0, 0, 0
		for i in xrange(len(s)):
			if s[i] == '(':
				vec.append(i)

			else:
				if len(vec) == 0:
					accumlen = 0
				else:
					matchPos = vec.pop()
					matchlen = i - matchPos + 1
					if len(vec) == 0:
						accumlen += matchlen
						matchlen = accumlen
					else:
						matchlen = i - vec[-1]

					maxlen = max(maxlen, matchlen)
					

		return maxlen