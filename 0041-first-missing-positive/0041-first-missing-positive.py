class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while (
                1<=nums[i]<=n and
                nums[nums[i]-1] != nums[i]
            ):
                correctindex = nums[i]-1
                nums[i], nums[correctindex] = nums[correctindex], nums[i]

        for i in range(n):
            if nums[i] != i+1:
                return i+1
        
        return n+1

        # Time : O(N)
        # Space : O(1)