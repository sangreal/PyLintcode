class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 0:
            return 0
        if len(timeSeries) == 1:
            return duration

        ans = duration
        for i in xrange(1, len(timeSeries)):
            cur = min(duration, timeSeries[i] - timeSeries[i-1])
            ans += cur
        return ans
