class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        m = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                if profit > m:
                    m = profit
            else:
                l = r
            r += 1
        return m