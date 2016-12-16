class Trie(object):
    def __init__(self):
        self.vec = [None for i in xrange(2)]

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = 0

        root = Trie()
        for num in nums:
            curNode = root
            for i in xrange(31, -1, -1):
                curIdx = (num >> i) & 1
                if curNode.vec[curIdx] == None:
                    curNode.vec[curIdx] = Trie()
                curNode = curNode.vec[curIdx]

        for num in nums:
            cursum = 0
            curNode = root
            for i in xrange(31, -1, -1):
                idx = (num >> i) & 1
                if curNode.vec[idx^1] != None:
                    cursum += (1 << i)
                    curNode = curNode.vec[idx^1]
                else:
                    curNode = curNode.vec[idx]
            maxsum = max(maxsum, cursum)

        return maxsum
