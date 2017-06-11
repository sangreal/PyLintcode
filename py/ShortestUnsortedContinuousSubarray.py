class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lidx, ridx = -1, -1
        l, r = 0, len(nums)-1
        while l < r and (lidx < 0 or ridx < 0):
            if nums[l+1] >= nums[l]:
                l += 1
            elif lidx < 0:
                lidx = l

            if nums[r-1] <= nums[r]:
                r -= 1
            elif ridx < 0:
                ridx = r

        return ridx - lidx + 1

if __name__ == "__main__":
    s = Solution()
    slist = [2,6,4,8,10,9,15]
    ans = s.findUnsortedSubarray(slist)
    print 'the ans is : %d' %(ans)
