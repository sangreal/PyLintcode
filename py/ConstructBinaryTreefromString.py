# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findlpos(self, st):
        cnt = 0
        pos = len(st) - 1
        while pos > 0:
            if st[pos] == ')':
                cnt += 1
            elif st[pos] == '(':
                cnt -= 1
            if cnt == 0:
                break
            pos -= 1
        return pos

    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if len(s) == 0:
            return None

        rootval = s[0]
        root = TreeNode(rootval)
        rstartpos = self.findlpos(s)
        lendpos = rstartpos-1
        if len(s) > 2:
            root.left = self.str2tree(s[2:rstartpos])
            root.right = self.str2tree(s[rstartpos:])
        return root
