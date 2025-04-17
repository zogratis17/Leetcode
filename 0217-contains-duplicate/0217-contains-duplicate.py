class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for element, freq in count.items():
            if freq > 1:
                return True

        return False

        # Time : O(N)
        # Space : O(N)