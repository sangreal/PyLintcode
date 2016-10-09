import collections

class Solution(object):
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

    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        storedict = collections.defaultdict(list)
        for c in strings:
            newstr = self.getOrigin(c)
            storedict[newstr].append(c)

        retlist = []
        for v in storedict.itervalues():
            retlist.append(v)
        return retlist
