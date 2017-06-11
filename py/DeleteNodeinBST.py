# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        parent = None
        target = root
        while target.val != key:
            parent = target
            if target.val < key:
                target = target.right
            else:
                target = target.left
        prev, node = None, None
        if target.left:
            node = target.left
            while node.right:
                prev = node
                node = node.right
            if prev:
                prev.right = node.left
            node.right = target.right
            node.left = target.left
        else:
            node = target.right
            while node.left:
                prev = node
                node = node.left
            if prev:
                prev.left = node.right
            node.right = target.right
            node.left = target.left
        if parent is not None:
            if parent.left == target:
                parent.left = node
            else:
                parent.right = node
        return node if target == root else root

