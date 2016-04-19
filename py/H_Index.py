class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        citations.sort(reverse = True)
        idx = 0

        for x in xrange(len(citations)):
            if citations[x] >= x:
                idx += 1
        return idx
