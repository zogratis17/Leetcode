class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        start = prices[0]
        len1 = len(prices)

        for i in range(len1):
            if start < prices[i]:
                max += prices[i] - start
            start = prices[i]
        return max