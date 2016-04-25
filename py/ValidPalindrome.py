class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if len(s) is 0:
        	return True

        l, r = 0, len(s)-1

        while l < r:
        	while l < r and s[l].isalpha() == False and s[l].isdigit() == False:
        		l += 1

        	if l == len(s)-1:
        		return True
        	while l < r and s[r].isalpha() == False and s[r].isdigit() == False:
        		r -= 1

        	if l < r:
        		if s[l].lower() != s[r].lower():
        			return False
        		else:
        			l += 1
        			r -= 1

        return True
