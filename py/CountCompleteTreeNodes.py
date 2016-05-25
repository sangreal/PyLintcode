# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        lnode, rnode = root, root
        hl, hr = 0, 0
        while lnode:
            lnode = lnode.left
            hl += 1
        while rnode:
            rnode = rnode.right
            hr += 1

        if hl == hr:
            return 2 << hl - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
