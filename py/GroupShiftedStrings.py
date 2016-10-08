import collections

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        storeVec = collections.defaultdict(list)
        for s in strings:
        	shift = tuple([(ord(c)-ord(s[0]))%26 for c in s])
        	storeVec[shift].append(s)

        return map(sorted, storeVec.values())