class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        n = len(prices)

        bd = 0
        sd = 0
        profit = 0

        for i in range(1, n):
            if prices[i] >= prices[i - 1]:
                sd += 1
            else:
                profit += prices[sd] - prices[bd]
                bd = i
                sd = i

        profit += prices[sd] - prices[bd]

        return profit