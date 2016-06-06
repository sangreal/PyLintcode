class Solution:
	"""
	@param S: A set of numbers.
	@return: A list of lists. All valid subsets.
	"""
	def dfs(self, s, tlen, curlist, retlist):
		if len(curlist) == tlen:
			retlist.append(curlist)
			return
		for i in xrange(len(s)):
			if i > 0 and s[i] == s[i-1]: continue
			self.dfs(s[i+1:], tlen, curlist + [s[i]], retlist)

	def subsetsWithDup(self, S):
		retlist = [[]]
		S.sort()
		for i in xrange(1, len(S)+1):
			self.dfs(S, i, [], retlist)
		return retlist 