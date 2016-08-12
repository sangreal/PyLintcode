class ZigzagIterator(object):
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1, self.v2 = v1, v2
        self.idx1, self.idx2 = 0, 0
        self.len1, self.len2 = len(v1), len(v2)
        

    def next(self):
        """
        :rtype: int
        """
        hasElem1 = True if self.idx1 < self.len1 else False
        hasElem2 = True if self.idx2 < self.len2 else False

        retnum = None
        if (self.idx1 <= self.idx2 or hasElem2 is False) and hasElem1:
            retnum = self.v1[self.idx1]
            self.idx1 += 1
        else:
            retnum = self.v2[self.idx2]
            self.idx2 += 1

        return retnum
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.idx1 < self.len1 or self.idx2 < self.len2 else False
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())