class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = len(prices) - 1
        return_set = set()
        if i == 0:
            return 0
        while i > 0:
            buy = min(set(prices[:i]))
            if buy >= prices[i]:
                return_set.add(0)
            else:
                return_set.add(prices[i] - buy)
            i -= 1
        return max(return_set)