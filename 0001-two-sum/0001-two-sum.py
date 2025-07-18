class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}
        for i, num in enumerate(nums):
            complement = target - num 
            if complement in mapper:
                return [mapper[complement], i]
            mapper[num] = i

            # Time : O(N)
            # Space : O(N)