import collections

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.storeQueue = collections.deque()
        self.popQueue = collections.deque()
        self.size = 0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """

        self.popQueue.append(x)

        while len(self.popQueue) > 1:
            self.storeQueue.append(self.popQueue.popleft())

        self.size += 1


    def pop(self):
        """
        :rtype: nothing
        """
        if self.size == 0:
            return

        if len(self.popQueue) == 0:
            while len(self.storeQueue) > 0:
                self.popQueue.append(self.storeQueue.popleft())
            while len(self.popQueue) > 1:
                self.storeQueue.append(self.popQueue.popleft())
        self.popQueue.popleft()

     
        self.size -= 1

    def top(self):
        """
        :rtype: int
        """
        if self.size == 0:
            return -1
        else:
           return self.popQueue[0]


    def empty(self):
        """
        :rtype: bool
        """
        return self.size == 0