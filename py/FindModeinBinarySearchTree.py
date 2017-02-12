# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def modeHelper(self, root):
        if root == None:
            return -1, 0, 0
        lmaxval, lmaxcnt, lrootcnt = self.modeHelper(root.left)
        rmaxval, rmaxcnt, rrootcnt = self.modeHelper(root.right)

        rootcnt = 1
        if lmaxval != -1 and lmaxval == root.val:
            rootcnt += lmaxcnt
        if rmaxval != -1 and rmaxval == root.val:
            rootcnt += rmaxcnt
        curmaxcnt = max(lmaxcnt, rmaxcnt, rootcnt)
        curmaxval = root.val
        if curmaxcnt != rootcnt:
            if curmaxcnt == lmaxcnt:
                curmaxval = lmaxval
            else:
                curmaxval = rmaxval
        return curmaxval, curmaxcnt, rootcnt

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        retmaxval, retmaxcnt, rootcnt = self.modeHelper(root)
        return retmaxval
