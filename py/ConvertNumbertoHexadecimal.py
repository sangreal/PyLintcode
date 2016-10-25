class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        bitmask = 0x0000000f
        retlist = []
        hexmap = {}
        for i in xrange(16):
            hexmap[i] = str(hex(i)[2:])

        if num < 0:
            num += 0x100000000

        while num > 0:
            curnum = num & bitmask
            retlist = [hexmap[curnum]] + retlist
            num >>= 4

        return ''.join(retlist) if retlist else '0'
