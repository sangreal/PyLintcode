class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return None
        rows, cols = len(matrix), len(matrix[0])
        isUp = False
        totalcnt = rows * cols
        while totalcnt > 0:
            if isUp:

