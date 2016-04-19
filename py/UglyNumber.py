class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
        	return False

        isugly = True

        while num > 1:
        	if num % 2 == 0:
        		num /= 2
        	elif num % 3 == 0:
        		num /= 3
        	elif num % 5 == 0:
        		num /= 5
        	else:
        		isugly = False
        		break;
        return isugly