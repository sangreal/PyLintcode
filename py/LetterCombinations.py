class Solution(object):
	def dfs(self, digits, curStr, ldict, retList):
		if len(digits) == 0:
			retList.append(curStr)
			return 

		for c in ldict[digits[0]]:
			self.dfs(digits[1:], curStr+c, ldict, retList)

	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		ldict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
		retList = []
		if len(digits) == 0:
			return retList
		self.dfs(digits, '', ldict, retList)
		return retList