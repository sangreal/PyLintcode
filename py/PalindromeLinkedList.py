# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
        	return True
        
        listlen = 0
        node = head;
        while node is not None:
        	node = node.next;
        	listlen += 1

        isOdd = True if listlen%2 > 0 else False

        walker = head
        runner = head
        while runner.next is not None and runner.next.next is not None:
        	walker = walker.next
        	runner = runner.next.next

        prev = None
        cur = head;

        while prev is not walker:
        	late = cur.next
        	cur.next = prev
        	prev = cur
        	cur = late

        if isOdd is True:
        	walker = walker.next

        while cur is not None and walker is not None:
        	if cur.val != walker.val:
        		return False
        	cur = cur.next
        	walker = walker.next

        return True

