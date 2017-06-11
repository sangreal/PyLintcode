class Solution(object):
    curcnt = 0
    def backtrack(self, nums, visited, pos):
        if pos > len(nums):
            Solution.curcnt += 1
            return

        for i in xrange(len(nums)):
            if visited[i] == 1:
                continue
            if nums[i] % pos == 0 or pos % nums[i] == 0:
                visited[i] = 1
                self.backtrack(nums, visited, pos + 1)
                visited[i] = 0
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        nums = [0] * N
        visited = [0] * N
        for i in xrange(1, N+1):
            nums[i-1] = i
        self.backtrack(nums, visited, 1)
        return Solution.curcnt
