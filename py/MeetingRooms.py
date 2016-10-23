# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
	def canAttendMeetings(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: bool
		"""
		if len(intervals) == 0:
			return True

		intervals = sorted(intervals, key=lambda c: c.start)
		maxright = 0
		for c in intervals:
			if c.start >= maxright:
				maxright = c.end
			else:
				return False
		return True

