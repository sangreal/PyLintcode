class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.curx, self.cury = 0, 0
        self.vec2d = vec2d
        self.cnt = 0
        for i in xrange(len(vec2d)):
            for j in xrange(len(vec2d[i])):
                self.cnt += 1

    def next(self):
        """
        :rtype: int
        """
        while len(self.vec2d[self.cury]) == None:
            self.cury += 1
        retval = self.vec2d[self.cury][self.curx]
        if self.curx+1 < len(self.vec2d[self.cury]):
            self.curx += 1
        else:
            self.curx = 0
            self.cury += 1

        self.cnt -= 1
        return retval

    def hasNext(self):
        """
        :rtype: bool
        """
        return  self.cnt > 0