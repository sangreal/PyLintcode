# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):

    def buildVec(self, root):

        retVec, vec = [], []
        p = root;
        while len(vec) > 0 or p:
            if p:
                vec.append(p)
                p = p.left
            else:
                p = vec.pop()
                retVec.append(p)
                p = p.right
        return retVec


    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if root is None:
            return
        self.nodevec = self.buildVec(root)
        self.idx = 0

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < len(self.nodevec)

    def next(self):
        """
        :rtype: int
        """
        self.idx += 1

        return self.nodevec[self.idx-1].val