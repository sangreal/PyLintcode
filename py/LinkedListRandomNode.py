import random
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        k = 1
        cnt = 0
        retNode = 0
        curnode = self.head
        while curnode is not None:
            if cnt < k:
                retNode = curnode.val
            else:
                rrand = random.randint(0, cnt)
                if rrand < k:
                    retNode = curnode.val

            cnt += 1
            curnode = curnode.next
        return retNode
