# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def dfs(self, root, prev, curcnt, maxlist):
		if root is None:
			maxlist[0] = max(maxlist[0], curcnt)
			return
		if prev is None or root.val != prev.val:
			maxlist[0] = max(maxlist[0], curcnt)
			curcnt = 0
		curcnt += 1
		self.dfs(root.left, root, curcnt, maxlist)
		self.dfs(root.right, root, curcnt, maxlist)

		return
	def longestConsecutive(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		maxlist = [0]*1
		self.dfs(root, None, 0, maxlist)
		return maxlist[0]