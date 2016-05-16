class Solution(object):
	def dfs(self, numstr, target, lastnum, curstr, retlist, strsum, pos):
		if len(numstr) == pos and target == strsum:
			retlist.append(curstr)
			print "print "
			return

		if len(numstr) <= pos:
			return

		print 'target is %d' %(target)
		for i in xrange(pos, len(numstr)):
			if i > pos and numstr[pos] == '0':
				break
			curnum = int(numstr[pos:i+1])
			print "curnum : %d" %(curnum)
			if pos == 0:
				self.dfs(numstr, target, curnum, curstr + "" + numstr[pos:i+1], retlist, curnum, i+1)
			else:
				self.dfs(numstr, target, curnum, curstr + "+" + numstr[pos:i+1], retlist, strsum+curnum, i+1)
				self.dfs(numstr, target, -curnum, curstr + "-" + numstr[pos:i+1], retlist, strsum-curnum, i+1)
				self.dfs(numstr, target, lastnum*curnum, curstr + "*" + numstr[pos:i+1], retlist, strsum-lastnum+lastnum*curnum, i+1)




	def addOperators(self, num, target):
		"""
		:type num: str
		:type target: int
		:rtype: List[str]
		"""
		retlist = []
		self.dfs(num, target, 0, "", retlist, 0, 0)
		return retlist

if __name__ == "__main__":
	s = Solution()
	inputstr = "105"
	target = 5
	retlist = []
	retlist = s.addOperators(inputstr, target)
	print 'return str %s len : %d' %("".join(retlist), len(retlist))