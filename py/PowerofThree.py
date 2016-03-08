class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        while n%3 == 0 and n > 0:
        	n /=3

        return n == 0