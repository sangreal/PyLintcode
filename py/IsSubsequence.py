class Solution(object):
	def isSubsequence(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		dp = [[0 for i in xrange(len(t)+1)] for j in xrange(len(s)+1)]
		for j in xrange(len(t)+1):
			dp[0][j] = 1
		for i in xrange(1, len(s)+1):
			for j in xrange(1, len(t)+1):
				if s[j-1] == t[i-1]:
					dp[i][j] |= dp[i-1][j-1]
				else:
					dp[i][j] = dp[i-1][j]

		return True if dp[len(s)][len(t)] == 1 else False
