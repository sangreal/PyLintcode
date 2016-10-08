# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def postOrderTraversal(self, root, nodelist):
		if root is None:
			return

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

	def upsideDownBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""