import collections

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def dfs(self, root):
		if root is None: return 0, 0

		l, nol = self.dfs(root.left)
		r, nor = self.dfs(root.right)

		return max(root.val + nol + nor, l+r), l+r
	def rob(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		maxret, tmp = self.dfs(root)
		return maxret