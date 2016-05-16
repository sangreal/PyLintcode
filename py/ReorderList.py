# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return

        walker, runner = head, head
        while runner.next and runner.next.next:
            walker = walker.next
            runner = runner.next.next

        mid = walker
        right = mid.next
        if right is None:
            return
        mid.next = None
        prev , cur = None, right
        while cur:
            later= cur.next
            cur.next = prev
            prev = cur
            cur = later

        first, second = head, prev
        i = 0
        while first and second:
            if i%2 ==0:
                later = first.next
                first.next = second
                first = later
            else:
                later = second.next
                second.next = first
                second = later
            i += 1
