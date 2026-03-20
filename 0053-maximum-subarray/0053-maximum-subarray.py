class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = max_global = nums[0]
        for i in range(1,len(nums)):
            curr_max = max(nums[i], curr_max+nums[i])
            max_global = max(curr_max, max_global)
    
        return max_global