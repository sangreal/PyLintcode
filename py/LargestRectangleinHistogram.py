class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
        vec = []
        h = len(heights)
        maxArea = 0
        for i in xrange(len(heights)):
            while len(vec) > 0 and heights[i] <= heights[vec[-1]]:
                idx = vec.pop()
                curArea = i*heights[idx] if len(vec) == 0 else (i-vec[-1]-1)*heights[idx]
                maxArea = max(maxArea, curArea)
            vec.append(i)

        while len(vec) > 0:
            idx = vec.pop()
            curArea = h*heights[idx] if len(vec) == 0 else (h-vec[-1]-1)*heights[idx]
            maxArea = max(maxArea, curArea)

        return maxArea
