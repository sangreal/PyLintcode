# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None

class Solution(object):
	def copyRandomList(self, head):
		"""
		:type head: RandomListNode
		:rtype: RandomListNode
		"""

		if head == None:
			return None

		cur = head
		while cur != None:
			newnode = RandomListNode(cur.label)
			newnode.next = cur.next
			cur.next = newnode
			cur = newnode.next

		cur = head
		while cur != None:
			cur.next.random = cur.random.next if cur.random != None else None
			cur = cur.next.next

		cur = head
		newhead = cur.next
		dummy = RandomListNode(-1)
		prenew = dummy
		while cur != None:
			prenew.next = cur.next
			prenew = cur.next
			cur.next = cur.next.next
			cur = cur.next
		return dummy.next