class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        firstmax, secondmax, thirdmax = -sys.maxint, -sys.maxint, -sys.maxint

        for n in nums:
            if n > firstmax:
                thirdmax = secondmax
                secondmax = firstmax
                firstmax = n
            elif n > secondmax and n < firstmax:
                thirdmax = secondmax
                secondmax = n
            elif n > thirdmax and n < secondmax:
                thirdmax = n

        return thirdmax if thirdmax != -sys.maxint else firstmax
