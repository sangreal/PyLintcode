class Solution:
	# @param {int} n a positive integer
	# @param {int[]} primes the given prime list
	# @return {int} the nth super ugly number
	def nthSuperUglyNumber(self, n, primes):
		idxlist = [0 for i in xrange(len(primes))]

		p = [1]

		minIdx, minVal = 0, 0

		for i in xrange(1, n):
			minVal = sys.maxint
			for j in xrange(len(primes)):
				if minVal > p[idxlist[j]]*primes[j]:
					minVal = p[idxlist[j]]*primes[j]
					minIdx = i
			p.append(minVal)
			idxlist[minIdx] += 1
		return p[-1]

