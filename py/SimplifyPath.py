class Solution(object):
	def simplifyPath(self, path):
		"""
		:type path: str
		:rtype: str
		"""
		if len(path) == 0:
			return None

		startC = False
		beginIdx = 0
		store = []

		retStr = ""
		for i in xrange(len(path)):
			if path[i] == "/":
				if startC == False:
					startC = True
					beginIdx = i
				else:
					if i > 1:
						if path[i-2] == "." and path[i-1] == ".":
							if len(store) > 0:
								store.pop()
							
						elif path[i-1].isalpha():
							elem = path[beginIdx:i]
							store.append(elem)

					if i > 0 and path[i-1] == "/":
						beginIdx = i

		for c in store:
			retStr += c
		return retStr if len(store) > 0 else "/"

