class Solution:
    def sortColors(self, nums):
        z, t, i = 0, len(nums) - 1, 0
        
        while i <= t:
            if nums[i] == 0:
                nums[i], nums[z] = nums[z], nums[i]
                z += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[t] = nums[t], nums[i]
                t -= 1
            else:
                i += 1

                # Time : O(N)
                # Time : O(1)