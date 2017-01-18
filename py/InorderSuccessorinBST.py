# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if root == None or p == None:
            return None

        storeVec = []
        cur = root
        while cur != None and cur != p:
            if cur.val < p.val:
                storeVec.append(cur)
                cur = cur.right
            else:
                storeVec.append(cur)
                cur = cur.left

        if p.right != None:
            rNode = p.right
            while rNode.left:
                rNode = rNode.left
            return rNode
        else:
            retNode = None
            while len(storeVec) > 0 and storeVec[-1].val < p.val:
                storeVec.pop()

            if len(storeVec) > 0:
                retNode = storeVec[-1]
            return retNode
