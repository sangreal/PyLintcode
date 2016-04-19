# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""

		prev, cur = None, head
		while cur is not None:
			later = cur.next
			cur.next = prev
			prev = cur
			cur = later

		return prev
        