# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
		"""
		:type root: TreeLinkNode
		:rtype: nothing
		"""
		
		if root == None:
			return
		curHead, lastHead = None, root
		pre = None

		while lastHead:
			lastcur = lastHead
			while lastcur:
				if lastcur.left:
					if curHead == None:
						curHead = lastcur.left
						pre = curHead
					else:
						pre.next = lastcur.left
						pre = pre.next
				if lastcur.right:
					if curHead == None:
						curHead = lastcur.right
						pre = curHead
					else:
						pre.next = lastcur.right
						pre = pre.next

				lastcur = lastcur.next

			lastHead = curHead
			curHead = None