class Solution(object):
	def calculate(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		def calcops(num1, num2, ops):
			if ops is '+':
				return num1+num2
			if ops is '-':
				return num1-num2
			return 0

		prevpos = 0
		beginDigit = False

		opslist = []
		numlist = []

		opsample = ['+', '-']

		for i in xrange(len(s)):
			if s[i].isdigit():
				if beginDigit == False:
					prevpos = i
					beginDigit = True
				if i == len(s)-1:
					curnum = int(s[prevpos:i+1])
					if len(opslist) > 0 and len(numlist) > 0:
						ops = opslist.pop()
						tmpnum = numlist.pop()
						numlist.append(calcops(tmpnum, curnum))
					else:
						numlist.append(curnum)
			else:
				curnum = int(s[prevpos:i])
				if len(opslist) > 0 and (s[i] == ')' or s[i] in opsample):
					ops = opslist.pop()
					tmpnum = numlist.pop()
					numlist.append(calcops(tmpnum, curnum))
				if s[i] in opsample:
					opslist.append(s[i])
				beginDigit = False
		return numlist[-1]


