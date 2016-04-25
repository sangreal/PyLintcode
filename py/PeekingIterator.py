import copy

# Below is the interface for Iterator, which is already defined for you.
#
class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.baseit = copy.deepcopy(iterator)
        self.advanceit = copy.deepcopy(iterator)

        self.nextval = sys.maxint
        if self.advanceit.hasNext():
            self.nextval = self.advanceit.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nextval

    def next(self):
        """
        :rtype: int
        """
        retval = self.baseit.next()
        if self.advanceit.hasNext():
            self.nextval = self.advanceit.next()
        return retval

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.baseit.hasNext()
