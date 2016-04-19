# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {string[]}

	def dfs(self, root, tmpstr, retList):
		if root is None:
			return
		if root.left is None and root.right is None:
			tmpstr += str(root.val)
			retList.append(tmpstr)
		tmpstr += str(root.val)
		self.dfs(root.left, tmpstr + '->', retList)
		self.dfs(root.right, tmpstr + '->', retList)
	def binaryTreePaths(self, root):
		retList = []
		self.dfs(root, "", retList)
		return retList
