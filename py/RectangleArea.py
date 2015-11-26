class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        dupArea = 0

        xmaxleft = max(A, E)
        xminright = min(C, G)
        ymaxbelow = max(B, F)
        yminupper = min(D, H)

        if xmaxleft < xminright and ymaxbelow < yminupper:
            dupArea = (xminright-xmaxleft)*(yminupper-ymaxbelow)

        Area1 = (C-A)*(D-B)
        Area2 = (G-E)*(H-F)
        return Area1+Area2-dupArea
