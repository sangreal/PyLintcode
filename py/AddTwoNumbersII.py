import collections
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1, stack2 = [], []
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        node1, node2 = l1, l2
        while node1:
            stack1.append(node1.val)
            node1 = node1.next
        while node2:
            stack2.append(node2.val)
            node2 = node2.next

        carry = 0
        retlist = collections.deque([])
        while len(stack1) > 0 or len(stack2) > 0:
            val1 = stack1.pop() if len(stack1) > 0 else 0
            val2 = stack2.pop() if len(stack2) > 0 else 0
            addval = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) / 10
            retlist.appendleft(ListNode(addval))
        if carry > 0:
            retlist.appendleft(ListNode(carry))
        return retlist
