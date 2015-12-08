class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
        	return 0;

        globalMax = nums[0]
        localMax = nums[0]
        localMin = nums[0]

        for i in xrange(1, len(nums)):
        	n = nums[i]
        	maxCopy = localMax
        	localMax = max(n, n*localMax, localMin*n)
        	localMin = min(n*maxCopy, n, localMin*n)
        	globalMax = max(globalMax, localMax)

        return globalMax