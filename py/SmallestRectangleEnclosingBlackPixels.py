class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        def getnext(image, x, y, nqueue):
            for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
                cx, cy = x + dx, y + dy
                if cx >= 0 and cy >=0 and cx < len(image) and cy < len(image[0]):
                    if image[cx][cy] == '1' and visited[cx][cy] == 0:
                        nqueue.append((cx, cy))

        queue = [(x, y)]
        minh, maxh, minv, maxv = x, x, y, y
        rows, cols = len(image), len(image[0])
        visited = [[0 for i in xrange(cols)] for j in xrange(rows)]
        while queue:
            nqueue = []
            while queue:
                curx, cury = queue.pop(0)
                visited[curx][cury] = 1
                getnext(image, curx, cury, nqueue)
                minh = min(minh, curx)
                maxh = max(maxh, curx)
                minv = min(minv, cury)
                maxv = max(maxv, cury)
            queue = nqueue
        return (maxh - minh + 1)*(maxv - minv + 1)
