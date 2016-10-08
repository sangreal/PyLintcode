
class Solution(object):
	def threeSumSmaller(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		retnum = 0
		nums = sorted(nums)
		lens = len(nums)
		for i in xrange(lens-2):
			j, k = i+1, lens-1
			while j < k:
				sums = nums[i]+nums[j]+nums[k]
				if sums < target:
					retnum += k-j
					j += 1
				else:
					k -= 1
		return retnum

