class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        firstmax = max(nums)
        index = nums.index(firstmax)
        del nums[index]
        secondmax = max(nums)

        if secondmax > firstmax/2:
            return -1
        else:
            return index