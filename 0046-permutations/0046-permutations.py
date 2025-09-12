class Solution(object):
    def permute(self, nums):
        result = []
        def f(start):
            if start >= len(nums):
                result.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]  
                f(start + 1)                               
                nums[i], nums[start] = nums[start], nums[i]
        f(0)
        return result