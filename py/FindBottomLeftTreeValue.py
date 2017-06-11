import collections
import copy

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return None

        storevec = collections.deque()
        storevec.append(root)
        nextvec = collections.deque()
        curnode = None

        while len(storevec) > 0:
            nextvec.clear()
            curnode = None
            while len(storevec) > 0:
                curnode = storevec.popleft()
                if curnode.right:
                    nextvec.append(curnode.right)
                    haschild = True
                if curnode.left:
                    nextvec.append(curnode.left)
                    haschild = True
n
            storevec = copy.copy(nextvec)
        return curnode.val

