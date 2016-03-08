class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        vec = [0 for i in xrange(26)]
        for i in xrange(len(words)):
          vec = [0 for i in xrange(26)]
          for x in words[i]:
            idx = ord(x)-ord('a')
            vec[idx] = 1

          collide = False
          maxval = 0
          for j in xrange(i+1, len(words)):
            for y in words[j]:
              idx = ord(y)-ord('a')
              if vec[idx] == 1:
                collide = True
            if collide == False:
              maxval = max(maxval, len(words[i])*len(words[j]))

        return maxval



