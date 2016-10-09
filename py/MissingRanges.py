class Solution(object):	def findMissingRanges(self, nums, lower, upper):
		"""
		:type nums: List[int]
		:type lower: int
		:type upper: int
		:rtype: List[str]
		"""
		l = lower
		N = len(nums)
		retlist = []
		if N == 0:
			if lower == upper:
				retlist.append(str(lower))
			else:
				tmpstr = str(lower) + '->' + str(upper)
				retlist.append(tmpstr)
			return retlist

		for i in xrange(N):
			if nums[i] == l:
				l += 1
			else:
				if nums[i]-l == 1:
					retlist.append(str(l))
				elif nums[i]-l > 1:
					tmpstr = str(l) + '->' + str(nums[i]-1)
					retlist.append(tmpstr)
				l = nums[i] + 1

		end = nums[N-1]
		if end < upper:
			if upper - end == 1:
				retlist.append(str(upper))
			else:
				tmpstr = str(end+1) + '->' + str(upper)
				retlist.append(tmpstr)

		return retlist
