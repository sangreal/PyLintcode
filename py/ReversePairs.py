class Solution:
	# @param {int[]} A an array
	# @return {int} total of reverse pairs
	def merge(self, start, mid, end, A):
		p, q = start, mid+1

		tmp = []

		cursum = 0
		while p <= mid and q <= end:
			if A[p] <= A[q]:
				tmp.append(A[p])
				p += 1
			else:
				tmp.append(A[q])
				q += 1
				cursum += mid-p+1

		while p <= mid:
			tmp.append(A[p])
			p += 1
		while q <= end:
			tmp.append(A[q])
			q += 1

		for i in tmp:
			A[start] = i
			start += 1

		return cursum


	def mergesort(self, start, end, A):
		if start >= end:
			return 0

		mid = (start + end)/2
		parisum = 0

		parisum += self.mergesort(start, mid, A)
		parisum += self.mergesort(mid+1, end, A)
		parisum += self.merge(start, mid, end, A)

		return parisum

	def reversePairs(self, A):
		return self.mergesort(0, len(A)-1, A)
