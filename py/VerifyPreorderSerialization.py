import collections

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        store = collections.deque()

        for item in preorder.split(','):
        	store.append(item)
        	while len(store) > 2 and store[-1] == '#' and store[-2] == '#' and store[-3] != '#':
    			store.pop()
    			store.pop()
    			store[-1] = '#'

    	return len(store) == 1 and store[0] == '#'
