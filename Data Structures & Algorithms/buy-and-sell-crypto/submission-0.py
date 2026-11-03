class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        diff = 0
        for price in prices:
            diff = max(diff, price-mini)
            mini = min(mini, price)
        return diff