# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	# @param {ListNode} head, a ListNode
	# @oaram {int} v1 an integer
	# @param {int} v2 an integer
	# @return {ListNode} a new head of singly-linked list
	def swapNodes(self, head, v1, v2):
		dummy = ListNode(-1)
		dummy.next = head
		p1, p2 = dummy, dummy

		while p1.next is not None and p2.next is not None and v1 != v2:
			if p1.next.val != v1:
				p1 = p1.next
			if p2.next.val != v2:
				p2 = p2.next

			if p1.next is not None and p2.next is not None and p1.next.val == v1 and p2.next.val == v2:
				prev1, prev2 = p1.next, p2.next
				p1.next = prev2
				p2.next = prev1

				p1next, p2next = prev1.next, prev2.next
				prev1.next = p2next
				prev2.next = p1next

		return dummy.next

