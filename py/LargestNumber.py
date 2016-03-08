class Solution(object):
	@staticmethod
	def compare(self, num1, num2):
		s1, s2 = str(num1), str(num2)
		newstr1, newstr2 = s1+s2, s2+s1
		return int(newstr1) > int(newstr2)

	def largestNumber(self, nums):

        nums.sort(cmp=compare)
        retstr = ''

        for i in xrange(len(nums)):
        	retstr += str(nums[i])
		return retstr