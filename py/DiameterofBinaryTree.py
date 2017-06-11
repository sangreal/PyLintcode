# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def traverse(self, root):
        if root is None:
            return 0, 0

        lcnt, lmaxsum = self.traverse(root.left)
        rcnt, rmaxsum = self.traverse(root.right)

        curcnt = 1 + max(lcnt, rcnt)
        return curcnt, max(1 + lcnt + rcnt, lmaxsum, rmaxsum)

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        curcnt, maxsum = self.traverse(root)
        return maxsum

