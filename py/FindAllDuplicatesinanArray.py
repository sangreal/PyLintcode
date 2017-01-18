class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        retvec = []

        for i in xrange(len(nums)):
            while nums[i] > 0 and nums[i] != i+1:
                if nums[i] == nums[nums[i]-1]:
                    retvec.append(nums[i])
                    nums[i] = 0
                else:
                    nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]

        return retvec
