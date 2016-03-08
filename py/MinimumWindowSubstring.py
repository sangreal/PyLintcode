class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        len_s, len_t = len(s), len(t)
        if len_t == 0 or len_s < len_t:
        	return ""

        countDict = dict()

        for x in t:
        	if x not in countDict:
        		countDict[x] = 0

        l, r = 0, 0
        count = len(countDict)
        cur = 0
        maxleft, maxright = 0, 0

        while r < len_s:
        	if s[r] in countDict:
        		if countDict[s[r]] == 0:
        			cur += 1
        		countDict[s[r]] += 1
        		if cur < count:
        			r += 1
        		while l < r:
        			if s[l] in countDict and countDict[s[l]] == 1:
        				break;
        			elif s[l] in countDict:
        				countDict[s[l]] -= 1
        			l += 1
        		maxleft, maxright = l, r

        	r += 1

        return s[maxleft:maxright-maxleft] if cur == count else ""

