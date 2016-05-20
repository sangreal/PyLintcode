class Solution(object):
	def threeSumClosest(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		mingap, ret = sys.maxint, 0
		leng = len(nums)
		i = 0
		nums = sorted(nums)
		while i < leng-2:
			j, k = i+1, leng-1
			while j < k:
				cursum = nums[i] + nums[j] + nums[k]
				gap = abs(target-cursum)
				if gap < mingap:
					mingap = gap
					ret = cursum
				if cursum <= target:
					j += 1
				else:
					k -= 1
			i += 1
		return ret