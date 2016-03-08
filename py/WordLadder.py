import string
import collections

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        visited = set(beginWord)
        def getNextWordList(tmpword):
            retvec = []
            for i in xrange(len(tmpword)):
                storeword = tmpword
                for c in list(string.lowercase):
                    tword = storeword
                    storeword = storeword[:i] + c + storeword[i+1:]
                    if storeword not in visited and storeword in wordList or storeword == endWord:
                        retvec.append(storeword)
                        visited.add(storeword)
                    storeword = tword
            return retvec

        curvec, nextvec = collections.deque(beginWord), collections.deque()
        level = 0
        found = False
        while len(curvec) > 0 and found == False:
            level += 1
            while len(curvec) > 0 and found == False:
                curword = curvec.popleft()
                tmpvec = getNextWordList(curword)
                for word in tmpvec:
                    if word == endWord:
                        found = True
                        break
                    else:
                        nextvec.append(word)
            curvec = list(nextvec)
            nextvec.clear()
        return 0 if found == False else level+1



