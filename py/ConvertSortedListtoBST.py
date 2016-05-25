# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None

        prev, walker, runner = None, head, head
        while runner.next and runner.next.next:
            prev = walker
            walker = walker.next
            runner = runner.next.next
        root = TreeNode(walker.val)

        if prev is None:
            root.left = None
        else:
            prev.next = None

            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(walker.next)

        return root
