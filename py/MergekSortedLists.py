import heapq
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergetwolists(self, node1, node2):
        dummy = ListNode(-1)
        curnode = dummy
        while node1 or node2:
            val1 = sys.maxint if node1 is None else node1.val
            val2 = sys.maxint if node2 is None else node2.val
            if val1 <= val2:
                curnode.next = node1
                curnode = curnode.next
                node1 = node1.next
            else:
                curnode.next= node2
                curnode = curnode.next
                node2 = node2.next
        return dummy.next
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return []
        retlist = lists[0]

        for i in xrange(1, len(lists)):
            retlist = self.mergetwolists(retlist, lists[i])
        return retlist

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return []
        heaplist = []
        for node in lists:
            if node:
                heaplist.append((node.val, node))

        heapq.heapify(heaplist)
        head = ListNode(-1)
        dummy = head
        while len(heaplist) > 0:
            topval, topnode = heapq.heappop(heaplist)
            dummy.next = topnode
            dummy = dummy.next

            if topnode.next:
                heapq.heappush(heaplist, (topnode.next.val, topnode.next))
        return head.next
