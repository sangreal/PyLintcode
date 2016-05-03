import heapq
import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = collections.defaultdict(int)
        for t in nums:
            d[t] += 1

        h = []
        for key, v in d.iteritems():
            if len(h) < k:
                heapq.heappush(h, (v, key))
            else:
                hv, hk = h[0]
                if hv < v:
                    heapq.heapreplace(h, (v, key))
        output = []
        while len(h) > 0:
            v, key = heapq.heappop(h)
            output.append(key)
        output.reverse()
        return output

if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    lists = s.topKFrequent(nums, 2)
    print 'the list is %s',lists
