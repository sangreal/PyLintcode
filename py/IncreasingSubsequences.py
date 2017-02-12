class Solution(object):
    def findHelper(self, nums, pos, curlist, retlist):
        if len(curlist) > 1:
            retlist.append(curlist)

        for i in xrange(pos, len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            curlist.append(nums[pos])
            self.findHelper(nums, pos+1, curlist, retlist)
            curlist.pop()
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        retlist = []
        curlist = []
        self.findHelper(sorted(nums), 0, curlist, retlist)
        return retlist
