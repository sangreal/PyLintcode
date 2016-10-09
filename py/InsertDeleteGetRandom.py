import collections
import random
class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storemap = collections.defaultdict(int)
        self.vec = []
        self.lens = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.storemap:
            self.storemap[val] = self.lens
            self.vec.append(val)
            self.lens += 1
            return True
        else:
            return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.storemap:
            idx = self.storemap[val]
            tail = self.vec.pop()
            if idx < len(self.vec):
                self.vec[idx] = tail
                self.storemap[tail] = idx
            del self.storemap[val]
            self.lens -= 1
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.vec)
        