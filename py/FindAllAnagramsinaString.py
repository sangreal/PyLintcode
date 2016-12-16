import collections

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        storemap = collections.defaultdict(int)
        for c in p:
            storemap[c] += 1

        storevec = []
        lens = len(p)
        curcnt = 0
        retlist = []
        for i in xrange(len(s)):
            if len(storevec) < lens:
                storevec.append(s[i])
                if s[i] in storemap:
                    if storemap[s[i]] > 0:
                        curcnt += 1
                    storemap[s[i]] -= 1
            else:
                if curcnt == lens:
                    retlist.append(i-lens)
                popInt = storevec.pop(0)
                if popInt in storemap:
                    storemap[popInt] += 1
                    if storemap[popInt] > 0:
                        curcnt -= 1
                storevec.append(s[i])
                if s[i] in storemap:
                    if storemap[s[i]] > 0:
                        curcnt += 1
                    storemap[s[i]] -= 1
        if curcnt == lens:
            retlist.append(len(s)-lens)
        return retlist
