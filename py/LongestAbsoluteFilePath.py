class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        if len(input) == 0 or '.' not in input:
            return 0
        if '\t' not in input:
            return len(input)
        strlist = input.split('\n\t')
        ans = [len(strlist[0]) + 1]

        def thisLevel(strs, level):
            nums = 0
            for i in xrange(len(strs)):
                if strs[i] == '\t':
                    nums += 1
            return True if nums == level else False

        def dfs(strlist, curlen, level, ans):
            print 'strlist : %s' %(strlist)
            if len(strlist) == 0:
                ans[0] = max(curlen, ans[0])
                return
            if '.' in strlist[0]:
                print '2 : %d' %(curlen)
                ans[0] = max(curlen + len(strlist[0].strip()), ans[0])
                return

            tmplist = []
            for i in xrange(len(strlist)):
                if thisLevel(strlist[i], level):
                    print 'strlist[i] : %s' %(strlist[i])
                    tmplist.append(i)
            for j in xrange(len(tmplist)):
                lens = len(strlist[tmplist[j]].strip())
                print 'strlist : %s curlen : %d  lens : %d' %(strlist[tmplist[j]], curlen, lens)
                if j < len(tmplist) - 1:
                    dfs(strlist[tmplist[j] + 1:tmplist[j+1]], curlen + lens + 1, level + 1, ans)
                else:
                    dfs(strlist[tmplist[j]+1:], curlen + lens + 1, level + 1, ans)
            return
        dfs(strlist[1:], ans[0], 0, ans)
        return ans[0]

if __name__ == '__main__':
    s = Solution()
    inputs = "dir\n    file.txt"
    ans = s.lengthLongestPath(inputs)
    print 'ans : %d' %(ans)
