class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        
        first_max = max(nums)
        nums.remove(first_max)
        try:
            second_max = max(nums)
            nums.remove(second_max)
            
            third_max = max(nums)

        except ValueError:
            return first_max
        return third_max

        