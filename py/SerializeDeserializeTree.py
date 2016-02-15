import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        vec = collections.deque([root])
        serialStr = ""

        while len(vec) > 0:
            curNode = vec.popleft()
            if curNode == None:
                serialStr += "null"
            else:
                serialStr += curNode.val
                vec.append(curNode.left)
                vec.append(curNode.right)

        return serialStr




    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """


        for i in xrange(len(data)):
            if data[i] == "null":
                continue

            curNode = TreeNode(data[i])
            lidx, ridx = 2*i+1, 2*i+2
            if lidx < len(data):
                if data[lidx] != "null":
                    curNode.left =
