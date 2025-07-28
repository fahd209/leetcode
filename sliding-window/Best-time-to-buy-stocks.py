class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            understand: i'm given an array prices of stocks. 
            the value of index is the price of the stock and the index is the day
            output: the best day to buy a stock for max profit. if 

            approach:
                 [7,1,5,3,6,4]
                  l r
        """
        n = len(prices)
        max_profit = 0
        l = 0

        for r in range(1, n):
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)

            if prices[l] > prices[r]:
                l = r
        return max_profit