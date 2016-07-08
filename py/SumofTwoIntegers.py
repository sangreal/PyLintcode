class Solution(object):
	def getSum(self, a, b):
		"""
		:type a: int
		:type b: int
		:rtype: int
		"""
		retval = 0x0
		carry = 0
		cnt = 0
		while a > 0 or b > 0:
			abit, bbit = a & 1, b & 1
			onecnt = 0
			if abit &1:
				onecnt += 1
			if bbit & 1:
				onecnt +=1
			if carry &1:
				onecnt += 1
			retval |= ((abit^bbit^carry) << cnt)
			if onecnt > 1:
				carry = 1
			else:
				carry = 0
			cnt += 1
			a >>= 1
			b >>= 1

		if carry & 1:
			retval |= (1 << cnt)
		return retval
