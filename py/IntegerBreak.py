class Solution(object):
	def integerBreak(self, n):
		"""
		:type n: int
		:rtype: int
		"""

		dp = [1] * (n+1)

		for i in xrange(1, n+1):
			for j in xrange(1, i+1):
				if i+j <= n:
					dp[i+j] = max(max(dp[i], i)*max(dp[j], j), dp[i+j])

		return dp[n]