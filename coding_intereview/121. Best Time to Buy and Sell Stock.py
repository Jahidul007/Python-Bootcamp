class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        buy = 9999999999999
        for i,j in enumerate (prices):
            if j<buy:
                buy = j
            else:
                if j>buy:
                    profit = max(profit, j-buy)
        return profit
      
