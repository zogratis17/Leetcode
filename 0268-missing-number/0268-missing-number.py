class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        setnums = set(nums)

        for i in range(len(nums)+1):
            if i not in setnums:
                return i
        return -1