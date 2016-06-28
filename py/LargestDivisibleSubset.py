class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []

        dp = [1 for i in xrange(n)]
        curnums = sorted(nums)
        parents = [-1 for i in xrange(n)]
        for i in xrange(1, n):
            for j in xrange(i):
                if curnums[i] % curnums[j] == 0:
                    if dp[i] < dp[j]+1:
                        dp[i] = dp[j]+1
                        parents[i] = j

        retlist = []
        maxidx, maxval = 0, dp[0]
        for i in xrange(n):
            if dp[i] > maxval:
                maxval = dp[i]
                maxidx = i

        while maxidx >= 0:
            retlist.append(curnums[maxidx])
            if parents[maxidx] == -1:
                break
            else:
                maxidx = parents[maxidx]
        return retlist

