class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
        	return 0
        l, r = 0, len(nums)-1

        minVal = nums[0]
        while l < r-1:
        	mid = l+(r-l)/2

        	if nums[mid] < nums[0]:
        		r = mid;
        	else:
        		l = mid;
        minVal = min(minVal, nums[l])
        minVal = min(minVal, nums[r])
        return minVal