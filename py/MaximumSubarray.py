class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if len(nums) == 0:
        	return 0

        globalMax, localsum = nums[0], nums[0]

        for i in xrange(1,len(nums)):
        	localsum = max(localsum+nums[i], nums[i])
        	globalMax = max(localsum, globalMax)
        return globalMax
