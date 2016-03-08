class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """

        tmpsum, ans = 0, 0
        for i in xrange(len(nums)):
            j = i
            tmpsum = 0
            while j < len(nums):
                tmpsum += nums[j]
                if tmpsum >= lower and tmpsum <= upper:
                    ans += 1

        return ans
