class Solution(object):

    def isValid(self, s):
        l = len(s)
        for x in xrange(len(s)):
            if s[x] != s[l-x-1]:
                return False
        return True

    def DFS(self, s, curlist):
        if len(s) == 0:
            Solution.retVec.append(curlist)
            return
        for x in xrange(1,len(s)+1):
            if self.isValid(s[:x]):
                self.DFS(s[x:], curlist+[s[:x]])

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        len_s = len(s)

        Solution.retVec = []
        self.DFS(s, [])
        return self.retVec
