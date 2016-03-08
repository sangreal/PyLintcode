class Solution:
    # @param {double} x the base number
    # @param {int} n the power number
    # @return {double} the result

    def CPow(self, x, n):
    	if (n == 0):
    		return 1

    	val = self.CPow(x, n/2);
    	if n%2 == 0:
    		return val*val
    	else:
    		return val*val*x

    def myPow(self, x, n):
        # Write your code here
        if n < 0:
        	return 1.0/self.CPow(x, -n);
        else:
        	return self.CPow(x, n)