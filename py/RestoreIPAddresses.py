class Solution:
    # @param {string} s the IP string
    # @return {string[]} All possible valid IP addresses

    def isValid(self, subs):
    	if len(subs) > 1 and subs[0] == '0':
    		return False

    	num = int(subs)
    	return num >= 0 and num < 256

    def backtrack(self, s, pos, vec, veclist):
    	if pos == 4:
    		if len(s) == 0:
    			vec = vec[:-1]
    			veclist.append(vec);
    		return

    	for x in xrange(1, 4):
    		subs = s[0:x]
    		if len(s) >= x and self.isValid(subs):
    			self.backtrack(s[x:], pos+1, vec + subs + '.', veclist)
    	return

    def restoreIpAddresses(self, s):
        # Write your code here
        veclist = []
        if len(s) == 0:
        	return veclist

        vec = ""
        self.backtrack(s, 0, vec, veclist)
        return veclist