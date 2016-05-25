# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i = 0
        retlist = []
        while i < len(intervals):
            if newInterval.end < intervals[i].start:
                retlist.append(newInterval)
                break
            elif newInterval.start > intervals[i].end:
                retlist.append(intervals[i])
            else:
                newInterval.start = min(newInterval.start, intervals[i].start)
                newInterval.end = max(newInterval.end, intervals[i].end)

            i += 1

        if i == len(intervals):
            retlist.append(newInterval)
        elif i < len(intervals):
            while i < len(intervals):
                retlist.append(intervals[i])
                i += 1
        return retlist
