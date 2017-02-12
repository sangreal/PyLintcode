import collections

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        storedict = collections.defaultdict(int)
        l = 0
        retlen = 0
        for r in xrange(len(s)):

            storedict[s[r]] += 1

            if len(storedict) > k:
                while l < r and len(storedict) > k:
                    storedict[s[l]] -= 1
                    if storedict[s[l]] == 0:
                        del storedict[s[l]]
                    l += 1
            retlen = max(retlen, r-l+1)
        return retlen
