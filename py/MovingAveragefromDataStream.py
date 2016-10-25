class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.vec = []
        self.size = size
        self.curcnt = 0
        self.cursum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.curcnt == self.size:
            self.cursum -= self.vec.pop(0)
            self.curcnt -= 1
        self.curcnt += 1
        self.cursum += val
        self.vec.append(val)
        return float(self.cursum)/self.curcnt



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)