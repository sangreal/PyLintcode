import collections

class KeyNode(object):
    def __init__(self, val, prev, next):
        self.val = val
        self.freq = 1
        self.prev = prev
        self.next = next

class FreqNode(object):
    def __init__(self, val, headnode, prev, next):
        self.freq = val
        self.headnode = headnode
        self.prev = prev
        self.next = next
        self.tailnode = headnode

    def insert(self, insernode):
        self.tailnode.next = insernode
        self.tailnode = insernode


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.keynodelist = collections.defaultdict(KeyNode)
        self.freqnodelist = collections.defaultdict(FreqNode)
        self.head = None
        self.capacity = capacity
        self.cnt = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keynodelist:
            return -1
        curkeynode = self.keynodelist[key]
        curkeynode.freq += 1
        self.unlink(curkeynode)
        self.link(curkeynode)
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cnt == self.capacity:
            curfreqnode = self.head
            todelval = curfreqnode.headnode.val
            curfreqval = curfreqnode.freq
            if curfreqnode.headnode == curfreqnode.tailnode:
                self.head = curfreqnode.next
                del self.freqnodelist[curfreqval]
            else:
                curfreqnode.headnode = curfreqnode.headnode.next

            del self.keynodelist[todelval]
            self.cnt -= 1
        if 1 not in self.freqnodelist:
            curnode = KeyNode(1, None, None)
            self.freqnodelist[1] = FreqNode(1, curnode, None, self.head)
            head = self.freqnodelist[1]
        else:
            tailn = self.freqnodelist[1].tailnode
            curnode = KeyNode(1, tailn, None)
            self.freqnodelist[1].tailnode = curnode
        self.cnt += 1



    def unlink(keynode):
        prevnode = keynode.prev
        nextnode = keynode.next
        if prevnode:
            prevnode.next = nextnode
        if nextnode:
            nextnode.prev = prevnode
    def link(keynode):
        curfreq = keynode.freq
        prevfreqnode = freqnodelist[curfreq-1]
        oldfreqnodenext = prevfreqnode.next
        if curfreq not in freqnodelist:
            freqnodelist[curfreq] = FreqNode(curfreq, keynode, prevfreqnode, oldfreqnodenext)
        prevfreqnode.next = freqnodelist[curfreq]