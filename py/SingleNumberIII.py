class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = reduce(lambda x, y: x^y, nums)
        lowbit = xor & -xor

        a = b = 0

        for n in nums:
        	if n & lowbit:
        		a ^= n
        	else:
        		b ^= n
        return [a, b]