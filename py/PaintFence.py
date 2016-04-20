class Solution:
    # @param {int} n non-negative integer, n posts
    # @param {int} k non-negative integer, k colors
    # @return {int} an integer, the total number of ways
    def numWays(self, n, k):
        if n == 0:
            return 0
        if n < 2:
            return k
        dp = [0 for i in xrange(n+1)]
        dp[0], dp[1], dp[2] = 0, k, k**2

        for i in xrange(3, n+1):
            dp[i] = (k-1)*dp[i-1] + (k-1)*dp[i-2]

        return dp[n]
