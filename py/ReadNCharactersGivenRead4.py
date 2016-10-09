# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
def read4(buf):
    return 0
class Solution(object):

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        if len(buf) == 0:
            return 0
        cnt = 0
        remain = 0
        cur = 1
        while cur > 0:
            cur = read4(buf)
            if cur == 4:
                cnt += 1
            else:
                remain = cnt
        return 4*cnt+remain
