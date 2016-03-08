class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
        	return 0

        sumstr = ''
        for x in xrange(1,n+1):
        	sumstr += str(x)

        count = 0

        for c in sumstr:
        	if c == '1':
        		count += 1
        return count