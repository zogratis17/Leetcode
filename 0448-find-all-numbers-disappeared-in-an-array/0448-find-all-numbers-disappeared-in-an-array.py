class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        snums = set(nums)
        res= []

        for i in range(1,n+1):
            if i not in snums:
                res.append(i)

        return res

        # Time :O(N)
        # Space : O(N)