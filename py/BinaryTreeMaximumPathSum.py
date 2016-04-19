import sys 
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def getSum(self, root):
		if root is None:
			return 0

		curstartval = root.val
		lmax = self.getSum(root.left)
		rmax = self.getSum(root.right)
		if lmax > 0 : curstartval += lmax
		if rmax > 0 : curstartval += rmax
		Solution.maxvalue = max(Solution.maxvalue, curstartval)

		return max(root.val, root.val+lmax, root.val+rmax)

	def maxPathSum(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		Solution.maxvalue = -sys.maxint
		retMax = self.getSum(root)
		return max(Solution.maxvalue, retMax)