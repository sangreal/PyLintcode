class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == k:
            return "0"
        while k > 0:
            i, lens = 0, len(num)
            while i < lens-1:
                if num[i] >= num[i+1]:
                    if k > 0:
                        k -= 1
                        lens -= 1
                        num = num[:i] + num[i+1:]
                        print "nums is ", num
                        i = i if i == 0 else i - 1
                    else:
                        break
                else:
                    i += 1
            if k > 0:
                num = num[:lens-1]
                k -= 1
        return str(int(num))

if __name__ == '__main__':
    t = Solution()
    num = "1111111"
    k = 3
    rerstr = t.removeKdigits(num, k)
    print "k is : ", rerstr
