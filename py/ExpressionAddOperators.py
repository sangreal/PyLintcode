class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        retlist = []
        def dfs(path, pos, cursum, lastnum):
            leng = len(num)
            if pos == leng and cursum == target:
                retlist.append(path)

            if pos >= leng:
                return

            for i in xrange(pos, leng):
                if i > pos and num[pos] == '0':
                    break

                curnum = int(num[pos:i+1])
                if pos == 0:
                    dfs(path + "" + str(curnum), i+1, curnum, curnum)
                else:
                    dfs(path + "+" + str(curnum), i+1, cursum+curnum, curnum)
                    dfs(path + "-" + str(curnum), i+1, cursum-curnum, -curnum)
                    dfs(path + "*" + str(curnum), i+1, cursum-lastnum+curnum*lastnum, curnum*lastnum)

        dfs("", 0, 0, 0)
        return retlist
