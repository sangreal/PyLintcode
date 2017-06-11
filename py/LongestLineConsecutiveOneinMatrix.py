class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if len(M) == 0 or len(M[0]) == 0:
            return 0

        ret = 0
        rows, cols = len(M), len(M[0])
        dialist = [0] * cols
        antilist = [0] * cols
        colist = [0] * cols
        for i in xrange(rows):
            currow = 0
            for j in xrange(cols):
                if M[i][j] == 1:
                    currow += 1
                    colist[j] += 1
                    antilist[j] = 1
                    if i > 0 and j < cols - 1:
                        antilist[j] += antilist[j + 1]
                    ret = max(ret, currow, colist[j])
                else:
                    currow, colist[j], antilist[j] = 0, 0, 0
            for k in xrange(cols - 1, -1, -1):
                if M[i][k] == 1:
                    dialist[k] = 1
                    if i > 0 and j > 0:
                        dialist[k] += dialist[k - 1]
                    ret = max(ret, dialist[k])
                else:
                    dialist[k] = 0
        return ret

