class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = float('inf')
        maxp = 0

        for p in prices:
            if p < curr:
                curr = p
            else:
                maxp = max(maxp, p - curr)
        
        return maxp