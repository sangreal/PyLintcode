import string
from sets import Set

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
				storeStr[i] = ch;
				if storeStr[i] == ch:
					continue
				elif storeStr == endWord or storeStr in wordList and storeStr not in visited:
					retVec.append(storeStr)
					visited.add(storeStr)

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