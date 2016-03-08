import collections

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ""

        for x in xrange(0, len(set(s))):
            top, idx = s[0], 0        	
            counter = collections.Counter(s)
        	for i in xrange(0, len(s)):
        		if top > s[i]:
        			top, idx = s[i], i
        		if counter[s[i]] == 1:
        			break
        		counter[s[i]] -= 1
        	ret += top
        	s = s[i+1:].replace(top, '')

        return ret