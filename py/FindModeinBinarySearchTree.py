# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def modeHelper(self, root, maxvalcnt, maxval, preval, curvalcnt, retlist):
        if root is None:
            return
        self.modeHelper(root.left, maxvalcnt, maxval, preval, curvalcnt, retlist)
        curvalcnt += 1

        if preval != root.val:
            curvalcnt = 1
            preval = root.val
        if curvalcnt > maxvalcnt:
            maxval = root.val
            del retlist[:]
            retlist.append(root.val)
            maxvalcnt = curvalcnt
        elif curvalcnt == maxvalcnt:
            retlist.append(root.val)
        self.modeHelper(root.right, maxvalcnt, maxval, preval, curvalcnt, retlist)
        return

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        maxvalcnt, maxval, preval, curvalcnt, retlist = 0, -1, -1, 0, []
        self.modeHelper(root, maxvalcnt, maxval, preval, curvalcnt, retlist)
        return retlist

