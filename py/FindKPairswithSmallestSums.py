import collections
import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        storeMap = collections.defaultdict(list)
        vec = []
        retlist = []
        if len(nums1) == 0 or len(nums2) == 0:
            return retlist

        i, j = 1, 1
        heapq.heapify(vec)
        retlist.append([nums1[0], nums2[0]])
        k -= 1
        while i < len(nums1) or j < len(nums2) and k > 0:
            if i <len(nums1):
                for k in xrange(j+1):
                    sum1 = nums1[i]+nums2[k]
                    heapq.heappush(vec, sum1)
                    storeMap[sum1].append([nums1[i], nums2[k]])
            if j < len(nums2):
                for t in xrange(i):
                    sum2 = nums1[t] + nums2[j]
                    heapq.heappush(vec, sum2)
                    storeMap[sum2].append([nums1[t], nums2[j]])
            elem = heapq.heappop(vec)
            retlist.append(storeMap[elem][0])

            storeMap[elem].pop(0)
            i += 1
            j += 1
            k -= 1

        while k > 0:
            elem = heapq.heappop(vec)
            retlist.append(storeMap[elem][0])

            storeMap[elem].pop(0)
            k -= 1
        return retlist
