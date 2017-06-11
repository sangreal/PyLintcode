import collections
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        storemap = collections.defaultdict(dict)
        for n in nums:
            l, h = n - 1, n + 1
            if n not in storemap:
                storemap[n] = {}
            if l not in storemap:
                storemap[l] = {}
            if h not in storemap:
                storemap[h] = {}
            storemap[n][1] += 1
            storemap[l][2] += 1
            storemap[h][0] += 1
        ans = 0
        for n in nums:
            ans = max(storemap[n][1] + storemap[n][0], storemap[n][1] + storemap[n][2], ans)
        return ans
