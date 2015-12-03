class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        vec = collections.deque()
        retlist = []

        for i in xrange(len(nums)):
        	if vec and vec[0] == i-k:
        		vec.popleft()
        	while vec and nums[vec[-1]] <= nums[i]:
        		vec.pop()

        	vec.append(i)
        	if i >= k-1:
        		retlist.append(nums[vec[0]])

        return retlist
