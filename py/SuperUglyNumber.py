class Solution:
    # @param {int} n a positive integer
    # @param {int[]} primes the given prime list
    # @return {int} the nth super ugly number
    def nthSuperUglyNumber(self, n, primes):
        if len(primes) == 0:
            return 1

        idxlist = [0 for i in xrange(len(primes))]
        q = [1]

        minint = sys.maxint
        for i in xrange(1, n):
            minint = sys.maxint
            for j in xrange(len(primes)):
                minint = min(minint, primes[j]*q[idxlist[j]])
            q.append(minint)
            for j in xrange(len(primes)):
                if minint == primes[j]*q[idxlist[j]]:
                    idxlist[j] += 1

        return q[-1]
