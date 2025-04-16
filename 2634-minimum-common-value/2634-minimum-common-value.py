class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        sn2 = set(nums2)

        for num in nums1:
            if num in sn2:
                return num
        
        return -1


        # Time : O(m + n)
        # Space : O(1)