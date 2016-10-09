# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findLargestHelper(self, root):
        if root is None:
            return 0, 0, 0, 0

        if root.left is None and root.right is None:
            return 1, 1, root.val, root.val

        lcnt, lmax, llow, lhigh = 0, 0, root.val, root.val
        rcnt, rmax, rlow, rhigh = 0, 0, root.val, root.val
        if root.left != None:
            lcnt, lmax, llow, lhigh = self.findLargestHelper(root.left)
        if root.right != None:
            rcnt, rmax, rlow, rhigh = self.findLargestHelper(root.right)


        curcnt, curmax = -1, max(lmax, rmax)
        if root.val >= lhigh and root.val <= rlow:
            if lcnt > -1 and rcnt > -1:
                curcnt = lcnt + rcnt + 1
                curmax = max(curmax, curcnt)

        return curcnt, curmax, llow, rhigh

    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        curcnt, curmax = -1, 0
        curcnt, curmax, _, _ = self.findLargestHelper(root)
        return curmax
