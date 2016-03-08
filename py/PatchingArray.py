class Solution(object):
    def dfs(self, nums, sumlist, cursum, cursize, fsize, n):
        if cursize == fsize and cursum <= n:
            sumlist[cursum] = 1
            return

        for x in nums:
            self.dfs(nums, sumlist, cursum+x, cursize+1, fsize)
        return


    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        if len(nums) == 0 or n == 0:
            return 0
        sumlist = [0 for x in xrange(n+1)]

        for x in xrange(1,len(nums)+1):
            self.dfs(nums, sumlist, 0, 0, x, n)

        isFilled = False
        hasHole = False
        minhole = -1
        retcount = 0
        while isFilled == False:
            hasHole = False
            for x in xrange(1, n+1):
                if sumlist[x] == 0:
                    minhole = x
                    hasHole = True
                    break

            if hasHole:
                for elem in sumlist:
                    sumlist[elem+minhole] = 1
                sumlist[minhole] = 1
                retcount += 1
            isFilled = True if hasHole == False else False
        return retcount

