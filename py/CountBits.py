class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        retlist = [0 for i in xrange(num+1)]

        pow2, before = 1, 1

        for x in xrange(1, num+1):
            if x == pow2:
                before = 1
                retlist[x] = 1
                pow2 <<= 1
            else:
                retlist[x] = 1 + retlist[before]
                before += 1
        return retlist
