class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        l, r = 0, len(nums)-1
        retlist = []

        while l <= r:
            lval = a*nums[l]**2 + b*nums[l] + c
            rval = a*nums[r]**2 + b*nums[r] + c
            if lval >= rval:
                if a > 0:
                    retlist.insert(0, lval)
                    l += 1
                else:
                    retlist.append(rval)
                    r -= 1
            else:
                if a > 0:
                    retlist.insert(0, rval)
                    r -= 1
                else:
                    retlist.append(lval)
                    l += 1
        return retlist
