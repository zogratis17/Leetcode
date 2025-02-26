class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        numscount = Counter(nums)
        for index,value in enumerate(nums):
            if numscount[value]>=n/2:
                return value
        return -1