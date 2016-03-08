import sys

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0: return 0

        l, r = 0, len(nums)-1

        minnum = nums[0]
        while l < r-1:
            m = l + (r-l)/2
            if nums[m] < nums[l]:
                minnum = min(minnum, nums[m])
                r = m-1
            elif nums[m] > nums[l]:
                minnum = min(minnum, nums[l])
                l = m+1
            else:
                l += 1

        minnum = min(minnum, nums[r])
        minnum = min(minnum, nums[l])
        return minnum
