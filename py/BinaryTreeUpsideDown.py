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

<<<<<<< HEAD
		if root.left is None and root.right is None:
			return root, root

		parent, newroot = self.helper(root.left)
		parent.right = root
		parent.left = root.right
		root.left, root.right = None, None
		return parent.right, newroot
=======
		p = root
		vec = []
		while p or len(vec) > 0:
			while p:
				vec.append(p)
				p = p.left

			q= None
			while len(vec) > 0:
				p = vec.pop()
				if p.right == q:
					nodelist.append(p)
					q = p
				else:
					vec.append(p)
					p = p.right
					break
	def buildTree(self, nodelist):
		if len(nodelist) == 0:
			return
		root = TreeNode(nodelist[0])
		root.left = 
>>>>>>> 466abae0f530262de89f274310aa5afd9fecaef1

	def upsideDownBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		newroot = None
		__ , newroot = self.helper(root)
		return newroot
