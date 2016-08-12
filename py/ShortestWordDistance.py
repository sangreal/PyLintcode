import cpllections

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        N = len(words)
        vec1, vec2 = [], []
        for i in xrange(N):
            if words[i] == word1:
                vec1.append(i)
            if words[i] == word2:
                vec2.append(i)

        mindis = sys.maxint

        m, n = 0, 0
        while m < len(vec1) and n < len(vec2):
            mindis = min(mindis, abs(vec1[m]-vec2[n]))
            if vec1[m] == vec2[n]:
                break
            elif vec1[m] < vec2[n]:
                m += 1
            else:
                n += 1
        return mindis

