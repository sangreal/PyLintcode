class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lens = len(s)

        if numRows == 1 or numRows >= lens:
            return s

        storevec = [[] for i in xrange(numRows)]
        row, step = 0, 1
        for c in s:
            storevec[row] += c
            if row == 0:
                step = 1
            elif row == numRows-1:
                step = -1
            row += step
        return ''.join(reduce(operator.add, storevec))
