class Solution:
    def countGood(self, nums, k):
        freq = {}
        total_pairs = 0
        left = 0
        result = 0
        for right in range(len(nums)):
            num = nums[right]
            if num in freq:
                total_pairs += freq[num]
                freq[num] += 1
            else:
                freq[num] = 1
            while total_pairs >= k:
                result += len(nums) - right
                left_num = nums[left]
                freq[left_num] -= 1
                total_pairs -= freq[left_num]
                left += 1
        return result

        # Time : O(N)
        # Space : O(N)