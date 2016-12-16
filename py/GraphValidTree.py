import collections

class Node(object):
    def __init__(self, val):
        self.val = val
        self.neighbors = []
class Solution(object):
    def initGraph(self, nodeStore, edges):
        for curlist in edges:
            first, second = curlist[0], curlist[1]
            if first not in nodeStore:
                nodeStore[first] = Node(first)
            if second not in nodeStore:
                nodeStore[second] = Node(second)
            nodeStore[first].neighbors.append(second)
            nodeStore[second].neighbors.append(first)

    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) == 0:
            return True

        nodeStore = collections.defaultdict(Node)
        self.initGraph(nodeStore, edges)
        visited = [0 for i in xrange(n)]
        def dfs(curnum, prevnum):
            if visited[curnum] == 1:
                return False
            visited[curnum] = 1
            neighbors = nodeStore[curnum].neighbors
            for n in neighbors:
                if n == prevnum:
                    continue
                if dfs(n, curnum) == False:
                    return False
            return True

        retFlag = dfs(0, -1)
        allVisited = True
        for n in visited:
            if n == 0:
                allVisited = False
                break
        return retFlag and allVisited



