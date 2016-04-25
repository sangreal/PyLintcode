# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def buildRecursive(self, preorderStr, inorderStr, prestart, preend, instart, inend):
		if prestart == preend or instart == inend:
			return None

		rootVal = preorderStr[prestart]
		rootNode = TreeNode(rootVal)
		inRootPos = instart
		while inorderStr[inRootPos] != rootVal:
			inRootPos += 1

		leftSize = inRootPos-instart

		rootNode.left = self.buildRecursive(preorderStr, inorderStr, prestart+1, prestart+leftSize+1, instart, inRootPos)
		rootNode.right = self.buildRecursive(preorderStr, inorderStr, prestart+leftSize+1, preend, inRootPos+1, inend)

		return root


	def buildTree(self, preorder, inorder):
		"""
		:type preorder: List[int]
		:type inorder: List[int]
		:rtype: TreeNode
		"""
		if len(preorder) == 0 or len(inorder) == 0: return None
		prestart, prend = 0, len(preorder)-1
		instart, inend = 0, len(inorder)-1
		return self.buildRecursive(preorder, inorder, prestart, prend, instart, inend)