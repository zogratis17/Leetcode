class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0
        l = r = 0
        
        while r < len(nums)-1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest, i+ nums[i])
            
            l=r+1
            r = farthest
            result+=1
        
        return result

        # Time : O(N)
        # Space : O(1)
        # Approach : Greedy - Simplified BFS 