class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        longest = 1
        for num in s:
            if num - 1 not in s:
                curr = 1
                while num+1 in s:
                    curr+=1
                    num+=1
                longest = max(curr,longest)
        return longest

# TC : O(n)
# SC : O(n)