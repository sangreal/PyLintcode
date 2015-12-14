import math

class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n):
        # Write your code here
        dicts = {}
        strval = str(n)
        sum = 0

        ret = True
        while sum != 1:
          sum = 0
          for x in strval:
            c = int(x)
            sum += math.pow(float(c), 2)
          strval = str(int(sum))
          if dicts.has_key(strval):
            ret = False
            break
          else:
            dicts[strval] = True

        return ret
