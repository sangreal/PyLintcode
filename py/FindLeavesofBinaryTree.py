# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def removeRoot(self, root, curVec):
		if root is None:
			return None
		if root.left is None and root.right is None:
			curVec.append(root.val)
			return None

		root.left = self.removeRoot(root.left, curVec)
		root.right = self.removeRoot(root.right, curVec)

		return root

	def findLeaves(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		retVec = []
		while root:
			curVec = []
			root = self.removeRoot(root, curVec)
			retVec.append(curVec)
		return retVec