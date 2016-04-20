import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def recoverTree(self, root):
		"""
		:type root: TreeNode
		:rtype: void Do not return anything, modify root in-place instead.
		"""
		if root is None: return

		vec = []
		prev = None
		node1, node2 = None,None
		p = root

		count = 0
		while len(vec) > 0 or p is not None:
			if p is not None:
				vec.append(p)
				p = p.left
			else:
				p = vec.pop()
				if prev is None:
					prev = p
				else:
					if prev.val > p.val:
						count += 1
						if node1 is None:
							node1 = prev
							node2 = p
						elif count > 1:
							node2 = p
				prev = p
				p = p.right

		node1.val, node2.val = node2.val, node1.val
