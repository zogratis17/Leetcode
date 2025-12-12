class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nz , i = 0,0
        while i < len(nums):
            if nums[i] != 0:
                nums[nz],nums[i] = nums[i],nums[nz]
                nz+=1
            i+=1