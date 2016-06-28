class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 0):
            return 0
        bucvol, buclen = 2, 0
        minnum, maxnum = nums[0], nums[1]

        for i in nums:
            minnum = min(i, minnum)
            maxnum = max(i, maxnum)

        buclen = (maxnum-minnum)/(len(nums)+1)
        buckets = [[] for i in xrange(buclen+1)]

        for i in nums:
            pos = (i-minnum)/buclen
            if len(buckets[pos]) == 0:
                buckets[pos].append(i)
                buckets[pos].append(i)
            else:
                if i < buckets[pos][0]:
                    buckets[pos][0] = i;
                if i > buckets[pos][1]:
                    buckets[pos][1] = i

        prev, maxgap = 0, 0

        for i in xrange(1, len(buckets)):
            if len(buckets[i]) == 0:
                continue

            maxgap = max(maxgap, buckets[i][0]-buckets[prev][1])
            prev = i
        return maxgap

