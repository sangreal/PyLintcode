class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        cntlist = []
        for points in timePoints:
            strlist = points.split(':')
            val = 60*int(strlist[0]) + int(strlist[1])
            cntlist.append(val)

        mindiff = sys.maxint

        prev = None
        cntlist.sort()
        for cur in cntlist:
            if prev is not None:
                mindiff = min(mindiff, cur - prev)
            prev = cur
        mindiff = min(mindiff, 24 * 60 - cntlist[-1] + cntlist[0])
        return mindiff
