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

        curvec, nextvec = collections.deque(list), collections.deque(list)
        curvec.append(beginWord)
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

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
	def getNextWordList(self, word, wordList, endWord):
		storeStr = word;

		alphalist = list(string.ascii_lowercase)

		visited = Set([word]);
		retVec = []

		for i in xrange(0, len(word)):
			storeStr = word;
			for ch in alphalist:
				oldchar = storeStr[i]
				if storeStr[i] == ch:
					continue
                storeStr[i] = ch
                if storeStr == endWord or storeStr in wordList and storeStr not in visited:
					retVec.append(storeStr)
					visited.add(storeStr)
                storeStr[i] = oldchar

		return retVec

	def ladderLength(self, beginWord, endWord, wordList):
	    if len(wordList) == 0:
	        return 0
        if beginWord == endWord:
            return 0

        curList = [beginWord]
        nextList = []

        hasFound = False

        level = 0;
        while len(curList)>0 and hasFound is not True:
        	level += 1
        	while len(curList)>0 and hasFound is not True:
        		tmpword = curList.pop(0)
        		tmpList = getNextWordList(tmpword, wordList, endWord)
        		for x in tmpList:
        			if x == endWord:
        				hasFound = True
        				break
        			else:
        				nextList.append(x)
        	curList = list(nextList)
        	del nextList[:]
        return level+1 if hasFound == True else 0
