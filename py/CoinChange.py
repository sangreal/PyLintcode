class Solution(object):
    def coinChange(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""
		if amount == 0: return 0

		dp = [-1 for i in xrange(amount+1)]
		for i in coins:
			if i <= amount:
				dp[i] = 1

		for i in xrange(1, amount):
			if dp[i] == -1: continue
			for c in coins:
				nextpos = i+c
				if nextpos <= amount:
					if dp[nextpos] == -1: 
						dp[nextpos] = dp[i]+1
					else:
						dp[nextpos] = min(dp[nextpos], dp[i]+1)
		return dp[amount]

