import collections
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here    

        if len(nums) == 0:
        	return 0

        leftMax, rightMax = [0]*len(nums), [0]*len(nums)
        localsum, leftMax[0], rightMax[-1]= nums[0], nums[0], nums[-1]

        for i in xrange(1, len(nums)):
        	localsum = max(localsum+nums[i], nums[i])
        	leftMax[i] = max(localsum, leftMax[i-1])

        localsum = nums[-1]

        for j in xrange(len(nums)-2, -1, -1):
        	localsum = max(localsum+nums[j], nums[j])
        	rightMax[j] = max(localsum, rightMax[j+1])

        globalMax = -sys.maxint-1
        for t in xrange(len(nums)-1):
        	tmpsum = leftMax[t]+rightMax[t+1]
        	globalMax = max(globalMax, tmpsum)

        return globalMax


