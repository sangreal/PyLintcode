class Solution(object):
	def isPalindrome(self, word):
		i, j = 0, -1
		leng = len(word)
		while i < leng+j:
			if word[i] != word[j]:
				return False
		return True

	def palindromePairs(self, words):
    	"""
    	:type words: List[str]
    	:rtype: List[List[int]]
    	"""
    	retList = [[]]

    	for i in xrange(len(words)):
    		j = i+1
    		while j < xrange(len(words)):
    			tmpstr1, tmpstr2 = words[i]+[j], words[j]+words[i]
    			if self.isPalindrome(tmpstr1):
    				retList.append([i, j])
    			if self.isPalindrome(tmpstr2):
    				retList.append([j, i])

    	return retList