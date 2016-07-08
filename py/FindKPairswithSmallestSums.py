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
        vec = []
        retlist = []
        dx, dy = [0, 1], [1, 0]
        if len(nums1) == 0 or len(nums2) == 0:
            return retlist
        storeMap = collections.defaultdict(list)

        len1, len2 = len(nums1), len(nums2)

        visited = [[0 for j in xrange(len2)] for i in xrange(len1)]
        visited[0][0] = 1

        vec.append(nums1[0]+nums2[0])
        storeMap[nums1[0]+nums2[0]].append([0, 0])
        heapq.heapify(vec)


        while len(vec) > 0 and k > 0:
            cur = heapq.heappop(vec)
            idx1, idx2 = storeMap[cur][0][0], storeMap[cur][0][1]
            storeMap[cur].pop(0)

            retlist.append([nums1[idx1], nums2[idx2]])
            for i in xrange(2):
                x, y = idx1+dx[i], idx2+dy[i]
                if x < len1 and y < len2 and visited[x][y] == 0:
                    heapq.heappush(vec, nums1[x]+nums2[y])
                    storeMap[nums1[x]+nums2[y]].append([x, y])
                    visited[x][y] = 1
            k -= 1

        return retlist
