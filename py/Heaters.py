import bisect

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        if len(houses) == 0 or len(heaters) == 0:
            return 0

        retval = 0
        heaters.sort()
        for h in houses:
            radius = 0x7FFFFFFF
            le = bisect.bisect_right(heaters, h)
            if (le > 0):
                radius = min(radius, h - heaters[le-1])
            ge = bisect.bisect_left(heaters, h)
            if ge < len(heaters):
                radius = min(radius, heaters[ge] - h)
            retval = max(retval, radius)
        return retval
