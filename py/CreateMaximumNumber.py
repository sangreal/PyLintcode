import collections

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def getMax(nums, t):
            store = []
            for i in xrange(len(nums)):
                while store and t-len(store) < len(nums)-i and nums[i] > store[-1]:
                    store.pop()
                if len(store) < t:
                    store.append(nums[i])
            return store

        def merge(nums1, nums2):
            retlist = []
            while len(nums1) > 0 and len(nums2) > 0:
                if nums1[0] >= nums2[0]:
                    retlist.append(nums1[0])
                    nums1 = nums1[1:]
                else:
                    retlist.append(nums2[0])
                    nums2 = nums2[1:]
            if len(nums1) > 0:
                retlist.extend(nums1)
            elif len(nums2) > 0:
                retlist.extend(nums2)
            return retlist

        retmax = []
        len1, len2 = len(nums1), len(nums2)
        for n in xrange(max(0, k-len2), min(k, len1)+1):
            tmplst = merge(getMax(nums1, n), getMax(nums2, k-n))
            retmax = max(tmplst, retmax)
        return retmax
