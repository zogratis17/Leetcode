class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        firstmax = max(nums)
        index = nums.index(firstmax)
        del nums[index]
        secondmax = max(nums)

        if firstmax >= secondmax*2:
            return index
        else:
            return -1