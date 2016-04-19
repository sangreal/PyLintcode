class Solution(object):
	"""
	@param {int[]} nums a list of integer
	@return nothing, modify nums in-place instead
	"""
	def wiggleSort(self, nums):
		tmp = sorted(nums)
		first, second  = (len(nums)+1) >> 1, len(nums)

		for i in xrange(len(nums)):
			if i & 1 == 0:
				first -= 1
				nums[i] = tmp[first]
			else:
				second -= 1
				nums[i] = tmp[second]