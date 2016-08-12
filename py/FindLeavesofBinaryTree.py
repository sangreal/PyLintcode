import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nodestore = collections.defaultdict(int)
        retlist, curlist = [], []
        hasLeft = True
        def dfs(root, nodestore, curlist):
            if root is None or nodestore[root.val] == 1:
                return
            hasLeft = True
            if (root.left is None and root.right is None) or (nodestore[root.left] and nodestore[root.right]):
                curlist.append(root.val)
                nodestore[root.val] = 1
                return

            dfs(root.left, nodestore, curlist)
            dfs(root.right, nodestore, curlist)
            return
        while hasLeft:
            hasLeft = False
            dfs(root, nodestore, curlist)
            retlist.append(curlist)
            curlist = []
        return retlist




