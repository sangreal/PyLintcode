import collections

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        store = collections.defaultdict(int)
        for c in s:
            store[c] += 1

        ret = True
        oddnum, oddtime, evennum = 0, 0, 0
        for v in store.itervalues():
            if v %2 == 1:
                oddtime += 1
                oddnum += v
            else:
                evennum += v

        if len(s) % 2 == 1:
            ret = True if oddtime == 1 and evennum+oddnum == len(s) else False
        else:
            ret = True if oddtime == 0 and evennum == len(s) else False

        return ret
