class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        # write your code here
        if len(height) == 0:
        	return 0

        length = len(height)
        globalMax = 0

        for i in xrange(0, length):
        	if i+1 < length and height[i] <= height[i+1]:
        		continue
        	minV = height[i]
        	for j in reversed(xrange(0, i+1)):
        		minV = min(height[j], minV)
        		area = minV*(i-j+1)
        		globalMax = max(globalMax, area)

        return globalMax