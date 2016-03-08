import sys

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    maxvalue = -sys.maxint
	def PathHelper(self, root):
	    if root is None:
        	return 0
        cval = root.val
        leftmax = self.PathHelper(root.left)
        if leftmax > 0:
        	cval += leftmax

        rightmax = self.PathHelper(root.right)
        if rightmax > 0:
        	cval += rightmax

        maxvalue = max(maxvalue, cval)

        return max(root.val, root.val+leftmax, root.val+rightmax)

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        connectMax = self.PathHelper(root)
        return max(connectMax, maxvalue)
