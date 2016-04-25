<<<<<<< HEAD
class Solution:
    # @param {int} num an integer
    # @return {boolean} true if num is an ugly number or false
    def isUgly(self, num):

        while num > 0:
            if num %5 == 0:
                num /= 5
            elif num %3 == 0:
                num /= 3
            elif num %2 == 0:
                num /= 2
            else:
                break

        return True if num == 1 else False
=======
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
>>>>>>> 67a0dfe3ae6a2caca9533a9364f0305e91aab015
