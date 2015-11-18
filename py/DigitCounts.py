class Solution:
    # @param k & n  two integer
    # @return ans a integer
    def digitCounts(self, k, n):
    	if n==0:
    		return 0
    	tmpstr = ''
    	numlist = []
    	for x in xrange(0,n+1):
    		tmpstr += (str(x))

    	count = 0
    	for c in tmpstr:
    		if str(k) == c:
    			count += 1

    	return count
