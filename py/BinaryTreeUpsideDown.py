# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def helper(self, root):
		if root is None:
			return root, None

		if root.left is None and root.right is None:
			return root, root

		parent, newroot = self.helper(root.left)
		parent.right = root
		parent.left = root.right
		root.left, root.right = None, None
		return parent.right, newroot

	def upsideDownBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		newroot = None
		__ , newroot = self.helper(root)
		return newroot
