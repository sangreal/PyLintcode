class SegmentTree(object):
	def __init__(self, start, end, count):
		self.start = start
		self.end = end
		self.count = count
		self.leftchild = None
		self.rightchild = None


class Solution(object):

	def buildSegmentTree(self, nums, start, end):
		if start > end:
			return None

		rootNode = SegmentTree(start, end, 0);
		if start == end:
			rootNode.count = 1 if nums[start] >= self.lower and nums[start] <= self.upper else 0
			return rootNode

		mid = (start+end)/2
		rootNode.leftchild = self.buildSegmentTree(nums, start, mid)
		rootNode.rightchild = self.buildSegmentTree(nums, mid+1, end)

		leftval = rootNode.leftchild.count if rootNode.leftchild != None else 0
		rightval = rootNode.rightchild.count if rootNode.rightchild != None else 0
		rootNode.count = leftval + rightval

		return rootNode

	def countRangeSum(self, nums, lower, upper):
		"""
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
		self.lower = lower
		self.upper = upper
		rootNode = self.buildSegmentTree(nums, 0, len(nums)-1)

		return rootNode.count