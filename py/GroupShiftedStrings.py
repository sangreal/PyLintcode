import collections

class Solution(object):
<<<<<<< HEAD
    def getOrigin(self, curStr):
        tmpStr = curStr
        valA = ord('a')
        while tmpStr[0] != 'a':
            for i in xrange(len(tmpStr)):
                if (tmpStr[i] == 'a'):
                    tmpStr[i] = 'z'
                else:
                    tmpStr[i] = chr(ord(tmpStr[i])-1)
        return tmpStr

=======
>>>>>>> 466abae0f530262de89f274310aa5afd9fecaef1
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
<<<<<<< HEAD
        storedict = collections.defaultdict(list)
        for c in strings:
            newstr = self.getOrigin(c)
            storedict[newstr].append(c)

        retlist = []
        for v in storedict.itervalues():
            retlist.append(v)
        return retlist
=======
        storeVec = collections.defaultdict(list)
        for s in strings:
        	shift = tuple([(ord(c)-ord(s[0]))%26 for c in s])
        	storeVec[shift].append(s)

        return map(sorted, storeVec.values())
>>>>>>> 466abae0f530262de89f274310aa5afd9fecaef1
