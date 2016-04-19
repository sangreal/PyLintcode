import collections

class Solution(object):

	def calcVal(self, v1, v2, ops):
		return {
			'+': lambda v1, v2: v1+v2,
			'-': lambda v1, v2: v2-v1,
			'/': lambda v1, v2: int(float(v2)/v1),
			'*': lambda v1, v2: v1*v2,
		}[ops](v1, v2)

	def evalRPN(self, tokens):
		"""
		:type tokens: List[str]
		:rtype: int
		"""
		if len(tokens) == 0:
			return -1
		st = []
		oplist = ['+', '-', '*', '/']
		for c in tokens:
			if c in oplist:
				val1, val2 = 0, 0
				if len(st) > 1:
					val1 = st.pop()
					val2 = st.pop()
					retval = self.calcVal(val1, val2, c)
					st.append(retval)
			else:
				st.append(int(c))
		return st[-1]

