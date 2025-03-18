from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        seen = {}
        sum_unique = 0
        
        # Count the occurrences of each number
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        # Sum the numbers that appear exactly once
        for num, count in seen.items():
            if count == 1:
                sum_unique += num
        
        return sum_unique