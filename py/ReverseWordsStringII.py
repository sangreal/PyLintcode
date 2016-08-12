class Solution(object):
    def reverseStr(self, s, l ,r):
        r -= 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        s.reverse()
        N = len(s)
        l, r = 0 , 0
        while l < N:
            while r < N and s[r] is not ' ':
                r += 1
            self.reverseStr(s, l, r)
            while r < N and s[r] is ' ':
                r += 1
            l = r
