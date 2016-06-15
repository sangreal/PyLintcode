import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maxheap = []
        self.minheap = []
        self.cnt = 0
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        self.cnt += 1
        heapq.heappush(self.minheap, num)
        mintop = self.minheap[0] if len(self.minheap) > 0 else None
        maxtop = self.maxheap[0] if len(self.maxheap) > 0 else -sys.maxint

        if -maxtop > mintop or len(self.maxheap)+1 < len(self.minheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        if len(self.minheap) < len(self.maxheap):
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.minheap) == 0:
            return 0

        if self.cnt % 2 == 0:
            return float((self.maxheap[0]+self.minheap[0])/2.0)
        else:
            return float(self.minheap[0])