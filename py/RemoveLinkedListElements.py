# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Includes import ListNode

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        dummy = ListNode(-1);
        dummy.next = head

        node = dummy
        isFound = False
        while node.next is not None:
        	if node.next.val is val:
        		curnode = node.next
        		node.next = node.next.next
        	else:
        		node = node.next

        return dummy.next