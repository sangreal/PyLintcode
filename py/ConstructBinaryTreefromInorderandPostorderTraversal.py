# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def build(self, instart, inend, poststart, postend):
        if poststart >= postend:
            return None

        root = TreeNode(self.postorder[postend-1])
        idx = self.inorder[instart:inend+1].index(root.val)
        root.left = self.build(instart, instart+idx, poststart, poststart+idx)
        root.right = self.build(instart+idx+1, inend, poststart+idx, postend-1)
        return root

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        self.inorder = inorder
        self.postorder = postorder
        return self.build(0, len(inorder), 0, len(postorder))