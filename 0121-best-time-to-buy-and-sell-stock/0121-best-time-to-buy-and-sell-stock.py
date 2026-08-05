class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lsf = float('inf')      
        op = 0                  
        pist = 0               

        n = len(prices)

        for i in range(n):
            if prices[i] < lsf:
                lsf = prices[i]

            pist = prices[i] - lsf

            if pist > op:
                op = pist

        return op