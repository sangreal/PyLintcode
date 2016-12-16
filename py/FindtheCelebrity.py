# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        cele = -1
        for i in xrange(n):
            hasFound = False
            known = False
            cnt = 0
            for j in xrange(n):
                if i != j and knows(i, j) or knows(j, i) == False:
                    break
                cnt += 1

            if cnt == n:
                cele = i
                break;
        return cele
