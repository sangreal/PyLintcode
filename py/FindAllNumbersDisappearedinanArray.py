class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        lens = len(nums)
        for i in xrange(lens):
            j = i
            while nums[j] != j+1:
                if nums[j] < 1 or nums[j] > lens or nums[nums[j]-1] == nums[j]:
                    break

                nums[nums[j]-1], nums[j] = nums[j],  nums[nums[j]-1]

        out = []
        for i in xrange(lens):
            if nums[i] != i+1:
                out.append(i+1)
        return out

if __name__ == "__main__":
    s = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    s.findDisappearedNumbers(nums)
