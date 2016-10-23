class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if len(heightMap) == 0:
            return 0

        yCnt, xCnt = len(heightMap), len(heightMap[0])
        globalmax = 0
        leftxmax = [0] * xCnt
        rightxmax = [0] * xCnt
        leftymax = [0] * yCnt
        rightymax = [0] * yCnt

        leftxmax[0] = heightMap[0][0]
        globalmax = leftxmax[0]
        for j in xrange(0, yCnt):
            globalmax = 0
            for i in xrange(1, xCnt):
                leftxmax[i] = globalmax
                globalmax = max(globalmax, heightMap[j][i])

        rightxmax = heightMap[0][xCnt-1]
        for j in xrange(0, yCnt):
            globalmax = 0
            for i in xrange(xCnt-2, 0, -1):
                globalmax = max(globalmax, heightMap[j])
