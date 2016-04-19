class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l, r = 0, len(citations)-1
        length = len(citations)-1
        while l <= r:
            mid = l + (r-l)/2
            idx = length-mid
            if citations[mid] >= idx+1:
                r = mid-1
            else:
                l = mid+1
        return length-l+1
