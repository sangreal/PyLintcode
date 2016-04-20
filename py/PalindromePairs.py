class Solution(object):
    def isPalindome(self, word):
        i, j = 0, -1
        while i < len(word)+j:
            if word[i] != word[j]: return False
            i+=1
            j-=1
        return True

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        retList = [[]]
        leng = len(words)
        for i in xrange(leng):
            j = i + 1
            while j < leng:
                tmp1, tmp2 = words[i]+words[j], words[j]+words[i]
                if self.isPalindome(tmp1):
                    retList.append([i, j])
                if self.isPalindome(tmp2):
                    retList.append([j, i])

                j+=1
        return retList
