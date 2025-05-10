class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        count_1=0
        count_2=0
        sum_1=0
        sum_2=0
        for i in nums1:
            if i==0:
                count_1+=1
            sum_1+=i
        for i in nums2:
            if i==0:
                count_2+=1
            sum_2+=i
        res=max(sum_1+count_1,sum_2+count_2)
        if not ((res==sum_1 or count_1) and (res==sum_2 or count_2)):
            return -1
        return res
        