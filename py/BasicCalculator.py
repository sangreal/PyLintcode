class Solution(object):

	def calcops(self, n1, n2, ops):
		if ops == '+':
			return n1+n2
		else:
			return n1-n2

	def isDigit(self, c):
		n = (int)c
		if n >= 0 and n <= 9:
			return True
		else:
			return False

	def isOps(self, op):
		return op == '+' or op == '-'

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num, ops = [], []

        strlen = len(s)
        number = ''
        for c in s:
        	if c == ' ':
        		continue
        	if c.isDigit():
        		number += c
        	else:
        		if number:
        			tmpnum = (int)number
        			num.append(tmpnum)
        			number = ''

        		if self.isOps(c):
        			ops.append(c)
	        	elif c == '(':
	        		num.append(c)
	        	elif c == ')':
					while len(num)>0 and len(ops)>0:
						
						n1 = num.pop()
						if n1 == '(':
							break
						n2 = num.pop()
						if n2 == '(':
							break
						opsc = ops.pop()
						newnum = calcops(n1, n2, opsc)
						num.append(newnum)
					num.pop()
				
				




