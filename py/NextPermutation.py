class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lens = len(nums)
        j = lens-2
        while j >= 0 and nums[j] >= nums[j+1]:
            j -= 1

        if j < 0:
            nums.reverse()
            return

        i = lens-1
        while i > j and nums[i] <= nums[j]:
            i -= 1

        nums[i], nums[j] = nums[j], nums[i]
        nums[j+1:] = reversed(nums[j+1:])
