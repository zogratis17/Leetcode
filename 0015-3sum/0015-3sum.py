from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                tot = nums[i] + nums[l] + nums[r]
                if tot == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    # Skip duplicates for left and right
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    # Move both pointers after processing
                    l += 1
                    r -= 1
                elif tot < 0:
                    l += 1
                else:
                    r -= 1

        return res
