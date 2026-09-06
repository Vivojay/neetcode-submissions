class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        running_min = 0
        max_profit = 0

        for i in range(l):
            if prices[running_min] > prices[i]: running_min = i
            p = prices[i] - prices[running_min]
            if max_profit < p: max_profit = p

        return max_profit
