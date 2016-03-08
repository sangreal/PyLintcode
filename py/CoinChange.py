class Solution(object):

    def dfs(self, coins, amount, num):
        if amount == 0:
            self.minNum = min(self.minNum, num)
            return
        for x in coins:
            if amount-x >= 0:
                self.dfs(coins, amount-x, num+1)
        return

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.minNum = sys.maxint

        self.dfs(coins, amount, 0)
        return -1 if self.minNum == sys.maxint else self.minNum
