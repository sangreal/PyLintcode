class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if len(s) == 0: return False

        size = len(s)
        visited = [0 for i in xrange(size+1)]
        visited[0] = 1
        for i in xrange(size):
            if visited[i] == 0:
                continue
            for word in wordDict:
                leng = len(word)
                if i + leng > size:
                    continue
                if s[i:i+leng] == word:
                    visited[i+leng] = 1

        return visited[size] == 1
