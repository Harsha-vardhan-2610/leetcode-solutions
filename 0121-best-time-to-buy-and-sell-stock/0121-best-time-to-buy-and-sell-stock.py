class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = prices[0], 0
        for num in prices:
            if num < min_price:
                min_price = num
            else:
                max_profit = max(max_profit, num - min_price)
        return max_profit