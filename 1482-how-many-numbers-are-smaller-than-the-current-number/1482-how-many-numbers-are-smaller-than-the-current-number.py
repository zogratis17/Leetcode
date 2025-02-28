class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = []
        a = sorted(nums)
        for i in nums:
            l.append(a.index(i))
        return l