class Solution(object):
    def quickselect(self, numlist, k):
        pivot = numlist[k-1]
        lstr, rstr = [], []
        lens = len(numlist)
        for i in xrange(lens):
            if numlist[i] < pivot:
                lstr.append(numlist[i])
            elif numlist[i]> pivot:
                rstr.append(numlist[i])

        if len(lstr) >= k:
            return self.quickselect(lstr, k)
        elif k > lens - len(rstr):
            return self.quickselect(rstr, k-(lens-len(rstr)))
        else:
            return pivot

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        numlist = []
        rowcnt, colcnt = len(matrix), len(matrix[0])

        for i in xrange(rowcnt):
            for j in xrange(colcnt):
                numlist.append(matrix[i][j])
        return self.quickselect(numlist, k)
