import collections

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.exStack = collections.deque()
        self.storeStack = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.storeStack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.exStack) == 0:
            for x in xrange(len(self.storeStack)):
                self.exStack.append(self.storeStack.pop())
        if len(self.exStack) > 0:
            self.exStack.pop()


    def peek(self):
        """
        :rtype: int
        """
        if len(self.exStack) == 0:
            for x in xrange(len(self.storeStack)):
                self.exStack.append(self.storeStack.pop())
        if len(self.exStack) > 0:
            return self.exStack[-1]
        else:
            return 0

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.exStack) == 0 and len(self.storeStack) == 0
