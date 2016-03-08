class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        retStr = []
        mapcnt = dict()

        mapdict = {'A':0, 'C':1, 'G':2, 'T':3}

        sum = 0
        for n in xrange(0, len(s)):
        	sum = (4*sum + mapdict[s[n]]) & 0xFFFFF
        	if n < 9:
        		continue
        	mapcnt[sum] = mapcnt.get(sum, 0) + 1
        	if mapcnt[sum] == 2:
        		retStr.append(s[n-9:n+1])

        return retStr