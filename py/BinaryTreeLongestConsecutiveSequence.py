# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.mindiff = sys.maxint
        self.last = -sys.maxint
        def calcDiff(root):
            if root is None:
                return
            calcDiff(root.left)
            self.mindiff = min(self.mindiff, root.val-self.last)
            self.last = root.val
            calcDiff(root.right)

        calcDiff(root)
        return self.mindiff
