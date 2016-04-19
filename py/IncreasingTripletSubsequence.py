class Solution(object):
    def increasingTriplet(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		if len(nums) < 3:
			return False

		curlist, candilist = [], []
		for i in xrange(len(nums)):
			if len(curlist) < 2:
				if len(curlist) < 1:
					curlist.append(nums[i])
				elif nums[i] < curlist[0]:
					curlist[0] = nums[i]
				elif nums[i] > curlist[0]:
					curlist.append(nums[i])
					candilist = list(curlist)
			else:
				if nums[i] > curlist[-1]:
					return True
				else:
					if nums[i] <= candilist[0]:
						candilist[0] = nums[i]
					elif nums[i] < candilist[1]:
						candilist[1] = nums[i]
						curlist = list(candilist)
		return False
