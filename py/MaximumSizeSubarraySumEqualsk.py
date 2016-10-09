import collections

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumstore = collections.defaultdict(list)
        cursum = 0
        for i in xrange(len(nums)):
            cursum += nums[i]
            sumstore[cursum].append(i)

        retval = 0
        for t in sumstore.keys():
            if t == k:
                retval = max(retval, sumstore[t][-1]+1)
            elif t-k in sumstore:
                retval = max(retval, sumstore[t][-1]-sumstore[t-k][0])
        return retval



