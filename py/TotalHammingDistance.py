class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        retcnt = 0
        for i in xrange(32):
            pos = (1 << i)
            zero, one = 0, 0
            for num in nums:
                if num & pos != 0:
                    one += 1
                else:
                    zero += 1
            retcnt += zero * one
        return retcnt
