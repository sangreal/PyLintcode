import collections

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

        storemap = collections.deque()
        storemap.append([root, 0])
        while len(storemap) > 0:
            curNode, level = storemap.popleft();
            if len(storemap) > 0 and storemap[0][1] == level:
                curNode.next = storemap[0]
            if curNode.left != None:
                storemap.append([curNode.left, level+1])
            if curNode.right != None:
                storemap.append([curNode.right, level+1])
