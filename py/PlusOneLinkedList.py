# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def plusOne(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		def reverse(head):
			prev, cur = None, head
			while cur:
				nextnode = cur.next
				cur.next = prev
				prev = cur
				cur = nextnode

			return prev

		newhead = reverse(head)
		carry = 0
		p = newhead
		p.val += 1
		prev = None
		while p:
			newval = carry+p.val
			carry = (newval)/10
			p.val = (newval)%10
			prev = p
			p = p.next
		if carry:
			prev.next = ListNode(carry)
		head = reverse(newhead)
		return head
        