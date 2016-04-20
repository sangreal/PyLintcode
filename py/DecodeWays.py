class Solution:
    # @param {string} s a string,  encoded message
    # @return {int} an integer, the number of ways decoding
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1 if int(s[0]) > 0 else 0

        dp = [0 for i in xrange(len(s)+1)]
        dp[0], dp[1] = 1, 1

        for i in xrange(2, len(s)+1):
            if 10 <=int(s[i-2:i]) <=26 and s[i-1] != '0':
                dp[i] = dp[i-1]+dp[i-2]
            elif int(s[i-2:i]) == 10 or int(s[i-2:i]) == 20:
                dp[i] = dp[i-2]
            elif s[i-1] != '0':
                dp[i] = dp[i-1]
            else:
                return 0

        return dp[len(s)]
