# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def traverse(root, curval):
            if not root:
                return 0

            res = 0
            if root.val == curval:
                res = 1
            res += traverse(root.left, curval-root.val)
            res += traverse(root.right, curval-root.val)
            return res

        if not root:
            return 0

        ans = traverse(root, sum)
        ans += self.pathSum(root.left, sum)
        ans += self.pathSum(root.right, sum)

        return ans
