import re
import collections

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0

        cntmap = collections.defaultdict(int)
        idxmap = collections.defaultdict(list)
        for i in xrange(len(s)):
            cntmap[s[i]] += 1
            idxmap[s[i]].append(i)

        hasLower = False
        candilist = []
        for k, v in cntmap.items():
            if v < k:
                hasLower = True
                candilist.extend(idxmap[k])

        if hasLower == False:
            return len(s)

        maxlen = 0
        sIdx = 0

        for i in sorted(candilist):
            if sIdx > i and sIdx > len(s)-1:
                break
            maxlen = max(self.longestSubstring(s[sIdx:i], k), maxlen)
            sIdx = i+1
        return maxlen
