# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
        	return head
        oddP, evenP = head, head.next

        evenH = evenP

        while oddP.next and oddP.next.next:
        	oddP.next = oddP.next.next
        	oddP = oddP.next
        	evenP.next = oddP.next
        	evenP = evenP.next

        oddP.next = evenH
        return head

