class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        storemap = {}
        stack = []
        for n in nums:
            while stack and stack[-1] < n:
                storemap[stack[-1]] = n
                stack.pop()
            stack.append(n)
        return [storemap.get(n, -1) for n in findNums]
