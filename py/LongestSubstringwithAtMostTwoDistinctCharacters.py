class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        cntstore = dict()
        curcount = 0
        l, r = 0, 0

        maxlen = 0
        while r < len(s):
            if s[r] not in cntstore or cntstore[s[r]] == 0:
                cntstore[s[r]] = 1
                curcount += 1
            else:
                cntstore[s[r]] += 1

            if curcount > 2:
                maxlen = max(maxlen, r-l)
                while cntstore[s[l]] > 0:
                    cntstore[s[l]] -= 1
                    if cntstore[s[l]] == 0:
                        break
                    l += 1
                l += 1
                curcount -= 1
            r += 1
        return max(maxlen, r-l)
