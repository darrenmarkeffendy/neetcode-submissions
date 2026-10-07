class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] <= lowest:
                lowest = prices[i]
            else:
                profit = prices[i] - lowest
                if  profit > max_profit:
                    max_profit = profit
        return max_profit
                