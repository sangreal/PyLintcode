import collections

class Solution(object):
	def dfs(self, store, n, curcnt, start):
		if curcnt == n: return True

		if start in store:
			for y, cnt in store[start].items():
				if cnt > 0:
					self.retList = self.retList + [y]
					store[start][y] -= 1
					if self.dfs(store, n, curcnt+1, y): return True
#					self.retList = self.retList[:-1]
#					store[start][y] += 1
		return False

	def findItinerary(self, tickets):
		"""
		:type tickets: List[List[str]]
		:rtype: List[str]
		"""

		store = collections.defaultdict(lambda: collections.OrderedDict())
		for l, r in sorted(tickets):
			store[l].setdefault(r, 0)
			store[l][r] += 1


		total = len(tickets)+1

		self.retList, start = ['JFK'], 'JFK'
		self.dfs(store, total, 1, start)
		return self.retList