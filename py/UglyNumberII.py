class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [1]
        i2, i3, i5 = 0, 0, 0
        while len(l) < n:
        	m1, m2, m3 = l[i2]*2, l[i3]*3, l[i5]*5
        	minval = min(m1, m2, m3)
        	if minval == m1:
        		i2 += 1
        	if minval == m2:
        		i3 += 1
        	if minval == m3:
        		i5 += 1
        	l.append(minval)

        return l[-1]