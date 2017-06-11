# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.mindiff = sys.maxint
        def calcDiff(root, parent):
            if root is None:
                return
            self.calcDiff(root.left, root)
            if parent is not None:
                mindiff = min(mindiff, abs(parent.val-root.val))
            self.calcDiff(root.right, root)

        calcDiff(root, None)
        return mindiff
