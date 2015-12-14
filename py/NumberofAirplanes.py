import collections
from operator import itemgetter

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end



class Solution:
    # @param airplanes, a list of Interval
    # @return an integer

    @staticmethod
    def cmp(a, b):
        """
        :type a: Interval
        :type b: Interval
        """
        if a.start != b.start:
            return a.start-b.start
        else:
            return a.end-b.end

    def countOfAirplanes(self, airplanes):
        # write your code here
        lists = []
        for x in airplanes:
        	lists.append((x.start, True))
        	lists.append((x.end, False))

        ret = 0
        pairnum = 0

        lists.sort(key=itemgetter(0, 1))
        print lists
        for (k, v) in lists:
        	if v:
        		pairnum += 1
        	else:
        		pairnum -= 1

        	ret = max(ret, pairnum)

        return ret

if __name__ == "__main__":
	Solution().countOfAirplanes([Interval(i[0], i[1]) for i in [[10,14],[10,15],[10,16],[1,10],[2,10],[3,10],[4,10]]])
