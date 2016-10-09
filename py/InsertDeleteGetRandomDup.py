import collections
import random

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storemap = collections.defaultdict(set)
        self.vec = []
        self.lens = 0

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        retval = True if val not in self.storemap else False
        self.storemap[val].add(self.lens)
        self.vec.append(val)
        self.lens += 1
        return retval

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.storemap:
            return False

        idx = self.storemap[val].pop()
        tail = self.vec[-1]
        self.vec[idx] = tail
        self.storemap[tail].add(idx)
        self.storemap[tail].remove(self.lens-1)

        del self.vec[-1]
        if not self.storemap[val]:
            del self.storemap[val]
        self.lens -= 1
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.vec)
