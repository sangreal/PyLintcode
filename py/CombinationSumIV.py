class Solution(object):
	def backtrack(self, nums, cursum, target, curlist, retlist, visited):
		if (cursum == target):
			retlist.append(curlist)
			return

		for i in xrange(len(nums)):
			if i > 0 and nums[i] == nums[i-1] or visited[i]:
				continue
			if cursum + nums[i] > target:
				break

			visited[i] = 1
			self.backtrack(nums, cursum+nums[i], target, curlist+[nums[i]], retlist, visited)
			visited[i] = 0

	def combinationSum4(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		curlist, retlist = [], []
		visited = [0] * len(nums)
		self.backtrack(sorted(nums), 0, target, curlist, retlist, visited)
		return len(retlist)
        