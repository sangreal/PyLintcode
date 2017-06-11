import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def helper(self, root, storemap):
        if root is None:
            return sys.maxint

        lval = self.helper(root.left, storemap)
        rval = self.helper(root.right, storemap)
        sumval = root.val
        if lval != sys.maxint:
            storemap[lval] += 1
            sumval += lval
        if rval != sys.maxint:
            storemap[rval] += 1
            sumval += rval
        storemap[sumval] += 1
        return sumval

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        storemap = collections.defaultdict(int)

        retlist = []
        self.helper(root, storemap)
        maxcur = 0
        for k, v in storemap.iteritems():
            if v > maxcur:
                retlist = [k]
                maxcur = v
            elif v == maxcur:
                retlist.append(v)
        return retlist
