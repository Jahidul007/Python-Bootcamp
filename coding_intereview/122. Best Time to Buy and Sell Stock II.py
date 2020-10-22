class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i,j in zip (prices, prices[1:]):
            print(i,j)
            if i< j:
                profit +=j-i
                    
        return profit
