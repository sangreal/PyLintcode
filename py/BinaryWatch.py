class Solution(object):
    def formOutputStr(self, cursum):
        retstr = ""
        minute, sec = cursum/60, cursum%60
        secstr = str(sec) if sec > 9 else "0" + str(sec)
        retstr = str(minute) + ":" + secstr
        return retstr

    def calcHelper(self, num, curidx, curcnt, cursum, retlist, digivec):
        if curidx > len(digivec)-1:
            return
        if curcnt == num:
            retlist.append(self.formOutputStr(cursum))
            return

        for i in xrange(curidx, len(digivec)):
            self.calcHelper(num, curidx+1, curcnt+1, cursum+digivec[i], retlist, digivec)
        return

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        digivec = [1, 2, 4, 8, 16, 32, 1*60, 2*60, 4*60, 8*60]
        retlist = []
        self.calcHelper(num, 0, 0, 0, retlist, digivec)
        return retlist
