# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        intervals.sort(lambda a, b: a.start-b.start)
        eraseCnt = 0
        prev = intervals[0]
        cur = None
        for i in xrange(1, len(intervals)):
            cur = intervals[i]
            if cur.start < prev.end:
                eraseCnt += 1
                if cur.end < prev.end:
                    prev = cur
            else:
                prev = cur
        return eraseCnt
