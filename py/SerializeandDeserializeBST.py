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
        if root is None:
            return '#'
        retstr = [str(root.val)]
        retstr.append(self.serialize(root.left))
        retstr.append(self.serialize(root.right))
        return ' '.join(retstr)



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        vals = iter(data.split())
        def doit():
            curval = next(vals)
            if curval == '#':
                return None
            root = TreeNode(int(curval))
            root.left = doit()
            root.right = doit()
            return root
        return doit()
