class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        if len(picture) == 0 or len(picture[0]) == 0:
            return 0

        rows, cols = len(picture), len(picture[0])
        rowcnts = [0]*rows
        colcnts = [0]*cols
        for i in xrange(len(picture)):
            for j in xrange(len(picture[0])):
                if picture[i][j] == 'B':
                    rowcnts[i] += 1
                    colcnts[j] += 1

        retval = 0
        for i in xrange(len(picture)):
            for j in xrange(len(picture[0])):
                if picture[i][j] == 'B' and rowcnts[i] == 1 and colcnts[j] == 1:
                    retval += 1
        return retval
