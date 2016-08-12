class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n
        tsum = 0
        while l<=r:
            mid = l+(r-l)/2
            if (mid == n):
                return tsum
            else:
                tsum += mid
                l = mid+1
        return tsum
