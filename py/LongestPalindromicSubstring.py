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

		dp[0][0] = 1
		for j in xrange(1,lens):
			dp[j][j-1] = 1 if s[j-1] == s[j] else 0

		leftIdx, rightIdx = 0 ,0
		for k in xrange(2, lens+1):
			for i in xrange(lens-k+1):
				if dp[i+1][i+k-2] == 1 and s[i] == s[i+k-1]:
					dp[i][i+k-1] = 1

				if rightIdx-leftIdx < k-1:
					leftIdx = i
					rightIdx = i+k-1

		return s[leftIdx:rightIdx+1]

