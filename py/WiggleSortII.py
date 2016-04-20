class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        store = sorted(nums)
        for i in xrange(1,len(nums), 2):
            nums[i] = store.pop()
        for j in xrange(0,len(nums),2):
            nums[j] = store.pop()
