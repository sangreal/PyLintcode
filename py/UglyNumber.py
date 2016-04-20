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
