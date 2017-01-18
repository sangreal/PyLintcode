import collections

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cntstore = collections.Counter()
        l, r = 0, 0
        retval = 0
        while r < len(s):
            cntstore[s[r]] += 1
            r += 1
            while r - l - max(cntstore.values()) > k:
                cntstore[s[l]] -= 1
                l += 1
            retval = max(retval, r-l)
        return retval
