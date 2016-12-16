import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class LevelTreeNode(TreeNode):
    def __init__(self, x, level):
        self.node = x
        self.level = level

class Solution(object):
    def traverseOrder(self, root, storedict):
        if root is None:
            return
        storevec = collections.deque()
        newRoot = LevelTreeNode(root, 0)
        storevec.append(newRoot)
        while len(storevec) > 0:
            curNode = storevec.popleft()
            rawNode = curNode.node
            curIdx = curNode.level
            storedict[curIdx].append(rawNode.val)
            if rawNode.left != None:
                leftNode = LevelTreeNode(rawNode.left, curIdx-1)
                storevec.append(leftNode)
            if rawNode.right != None:
                rightNode = LevelTreeNode(rawNode.right, curIdx+1)
                storevec.append(rightNode)

    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        storedict = collections.defaultdict(list)

        self.traverseOrder(root, storedict)
        retlist = []
        for k, v in sorted(storedict.iteritems()):
            retlist.append(v)
        return retlist
