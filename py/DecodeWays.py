class Solution:
	# @param {string} s a string,  encoded message
	# @return {int} an integer, the number of ways decoding
	def numDecodings(self, s):
		if len(s) == 0:
			return 0

		dp = [0 for i in xrange(len(s)+1)]
		for i in xrange(1, len(s)+1):
			if i == 0 and ord(s[i-1])-ord('0') > 0:
				dp[i] = 1
			if i > 1:
				dp[i] = dp[i-1]
				if ord(s[i-2]) > ord('0') and ord(s[i-2]) < ord('3') and ord(s[i-1]) < ord('7') and ord(s[i-1]) > ord('0'):
					dp[i] += 1

		return dp[i]