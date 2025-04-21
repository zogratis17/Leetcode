class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []

        for element , frequency in count.items():
            if frequency == 2:
                res.append(element)

        return res

        # Time : O(N)
        # Space : O(N)