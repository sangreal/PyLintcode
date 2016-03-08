class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        list1 = version1.split('.')
        list2 = version2.split('.')

        idx = 0
        len1 = len(list1)
        len2 = len(list2)
        maxlen = max(len1, len2)

        for i in xrange(maxlen):
            val1 = int(list1[i]) if i < len1 else 0
            val2 = int(list2[i]) if i < len2 else 0
            if val1 > val2:
                return 1
            elif val2 > val1:
                return -1
        return 0



