class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1
        maxProfit=0

        while r<len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                if profit > maxProfit:
                    maxProfit = profit
            else:
                l=r
            r+=1
        return maxProfit

        # Time : O(N)
        # Space : O(1)