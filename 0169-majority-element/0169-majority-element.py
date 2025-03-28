class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        n = len(nums)

        for key , value in count.items():
            if value > n/2:
                return key