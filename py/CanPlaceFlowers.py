class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed) == 0:
            return False
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        cnt = 0
        i = 1
        while i < len(flowerbed) - 1:
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i-1] == 0:
                cnt += 1
                flowerbed[i] = 1
                print 'i : %d' %(i)
                i += 2
            elif flowerbed[i+1] == 1:
                i += 3
            elif flowerbed[i] == 1:
                i += 2
            else:
                i += 1
        return True if cnt >= n else False

if __name__ == '__main__':
    s = Solution()
    lists = [1,0,0,0,0,1]
    s.canPlaceFlowers(lists, 2)
