class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def getnodes(lists):
            retlist = []
            cnt = 0
            for i in xrange(len(lists)):
                if lists[i] == '+':
                    cnt += 1
                else:
                    cnt = 0
                if cnt == 2:
                    retlist.append(i-1)
                    cnt = 1
            return retlist

        def backtrack(lists, player):
            canlist = getnodes(lists)
            for i in canlist:
                lists[i], lists[i+1] = '-', '-'
                ret = False
                if player == 1:
                    ret = False if backtrack(lists, 2) else True

                else:
                    ret = False if backtrack(lists, 1) else True

                lists[i], lists[i+1] = '+', '+'
                if ret:
                    return ret
            return False
        lists = list(s)
        return backtrack(lists, 1)

if __name__ == '__main__':
    s = Solution()
    strs = '+++++'
    ans = s.canWin(strs)
    print 'ans : %s' %(ans)
