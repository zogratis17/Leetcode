class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        sum = 0

        for key , val in count.items():
            if val == 1:
                sum += key
        
        return sum