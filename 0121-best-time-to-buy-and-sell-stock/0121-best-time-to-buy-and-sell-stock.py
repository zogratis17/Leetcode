class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r , maxProfit = 0 ,1 , 0

        while r < len(prices):
            if prices[r] > prices[l]:
                currProf = prices[r] - prices[l]
                maxProfit = max(currProf, maxProfit)
                r+=1
            else:
                l+=1
                r = l+1
        
        return maxProfit