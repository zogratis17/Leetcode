class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos,neg,res,i = [],[],[],0

        for num in nums:
            if num<0:
                neg.append(num)
            else:
                pos.append(num)
        
        while i<len(pos):
            res.append(pos[i])
            res.append(neg[i])
            i+=1
        
        return res

        # Time : O(N)
        # Space : O(N)