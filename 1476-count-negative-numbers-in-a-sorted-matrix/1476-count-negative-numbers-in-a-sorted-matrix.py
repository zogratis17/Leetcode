class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0 :
                    count +=1
        
        return count
# TC : O(M*N)
# SC : O(1)