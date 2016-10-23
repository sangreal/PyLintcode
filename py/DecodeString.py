<<<<<<< HEAD
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

=======
import collections

class Solution(object):
	def decodeString(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		if len(s) == 0:
			return None

		k = 1
		cntmap = collections.defaultdict(int)
		partmap = collections.defaultdict(str)

		for c in s:
			if c.isdigit():
				cntmap[k] = 10*cntmap[k] + int(c)
			elif c == '[':
				k += 1
			elif c == ']':
				partmap[k-1] += cntmap[k-1]*partmap[k]
				cntmap[k-1] = 0
				partmap[k] = ''
				k -= 1

			else:
				partmap[k] += c

		return partmap[1]
>>>>>>> 466abae0f530262de89f274310aa5afd9fecaef1
