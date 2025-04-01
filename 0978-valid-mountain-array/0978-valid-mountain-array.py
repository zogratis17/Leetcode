class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        l, r= 0, len(arr)-1

        while l+1<len(arr) and arr[l]<arr[l+1]:
            l+=1
        while r-1 > 0 and arr[r]<arr[r-1]:
            r-=1
        
        return l == r and l != 0 and r != len(arr) - 1

        # Time : O(N)
        # Space : O(1)