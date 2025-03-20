class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = Counter(nums)

        for key , value in count.items():
            if value > n/2:
                return key
        return 0