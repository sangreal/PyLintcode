class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        lens = len(s)
        l, r = 0, 2*k
        lists = list(s)
        while r <= lens:
            mid = l+k-1
            tl, tr = l, mid
            while tl < tr:
                lists[tl], lists[tr] = lists[tr], lists[tl]
                tl += 1
                tr -= 1
            l ,r = r, r + 2*k

        tl, tr = l, l
        if l+k < lens:
            tl, tr = l, l+k-1
        else:
            tl, tr = l, lens-1
        while tl < tr:
            lists[tl], lists[tr] = lists[tr], lists[tl]
            tl += 1
            tr -= 1
        return ''.join(lists)

if __name__ == "__main__":
    solut = Solution()
    st = "abcdefg"
    k = 2
    ret = solut.reverseStr(st, k)
    print 'tht sult is ' + ret

