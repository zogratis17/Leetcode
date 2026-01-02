class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        '''
        PigeonHole Principle : the repeated element must appear next to or very close to itself
        Time : O(N)
        Space : O(1)
        '''
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, min(i + 4, n)):
                if nums[i] == nums[j]:
                    return nums[i]
