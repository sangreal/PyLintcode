class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		lens = len(s)
		dp = [[0 for i in xrange(lens)] for j in xrange(lens)]

		for i in xrange(lens):
			dp[i][i] = 1


		leftIdx, rightIdx = 0 ,0
		maxlen = 0
		for j in xrange(lens-1, -1, -1):
			for i in xrange(j, lens):
				if s[i] == s[j] and (i-j <= 2 or dp[j+1][i-1]):
					if maxlen < i-j+1:
						maxlen = i-j+1
						leftIdx, rightIdx = j, i
					dp[j][i] = 1

		return s[leftIdx:rightIdx+1]




class Solution2(object):
	maxlen, maxl, maxr = 0, 0, 0
	def findmaxlen(self, s, lI, rI):
		lens = len(s)
		while lI-1 >= 0 and rI+1 < lens and s[lI-1] == s[rI+1]:
			lI -= 1
			rI += 1
		if Solution2.maxlen < rI-lI+1:
			Solution2.maxl = lI
			Solution2.maxr = rI
			Solution2.maxlen = rI-lI+1

	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		lens = len(s)

		for j in xrange(lens-1):
			li,ri = 0, 0
			if s[j] == s[j+1]:
				li, ri = j, j+1
				self.findmaxlen(s, li, ri)

			li, ri = j, j
			self.findmaxlen(s, li, ri)

		return s[Solution2.maxl:Solution2.maxr+1]
