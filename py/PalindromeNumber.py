class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        div = 1
        tmp = x
        while x/div > 0:
            div *= 10

        while x > 0:
            l ,r = x/div, x%10
            if l != r:
                return False
            x = x%div/10
            div /= 100
        return True
