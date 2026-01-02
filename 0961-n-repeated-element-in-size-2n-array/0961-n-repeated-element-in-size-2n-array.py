class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        c = Counter(nums)
        for num in nums:
            if c[num] == n:
                return num

# Time Complexity: O(N)

# Space Complexity: O(N)