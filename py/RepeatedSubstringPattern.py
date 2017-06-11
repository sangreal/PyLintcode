class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return False

        lens = len(s)
        if lens % 2 == 1:
            nodiff = True
            for i in xrange(1, lens):
                if s[i-1] != s[i]:
                    nodiff = False
                    break
            if nodiff:
                return nodiff

        s1, s2 = s[:lens/2], s[lens/2:]
        st1, st2, st3 = s[:lens/3], s[lens/3:lens*2/3], s[lens*2/3:]
        print "st1 : %s  st2 : %s  st3 : %s" %(st1, st2, st3)
        return s1 == s2 or st1 == st2 == st3

if __name__ == '__main__':
    s = Solution()
    strs = "bacbacbac"
    ret = s.repeatedSubstringPattern(strs)
    print 'ret : %r' %(ret)
