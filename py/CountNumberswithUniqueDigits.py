class Solution(object):
	def backtrack(self, curnum, visited, n, exlist):
		if curnum < 0 or curnum >= 10**n:
			return

		for i in xrange(10):
			if curnum == 0 and i == 0:
				continue

			prevnum = curnum
			curnum *= 10
			curnum += i
			if (curnum >= 10**n):
				break
			if visited[i] == 1:
				exlist.append(curnum)
			else:
				visited[i] = 1
				self.backtrack(curnum, visited, n, exlist)
				visited[i] = 0
			curnum = prevnum

		return



	def countNumbersWithUniqueDigits(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		exlist = []
		visited = [0]*10
		curnum = 0
		self.backtrack(curnum, visited, n, exlist)
		return 10**n-len(exlist)

class Solution(object):
	def countNumbersWithUniqueDigits(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		n = min(n, 10)
		nums = [1] + [9]*n

		for i in xrange(2, n+1):
			for j in xrange(9, 9-i+1, -1):
				nums[i] *= j

		return sum(nums[:n])

