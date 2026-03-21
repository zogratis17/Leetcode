class Solution:
    def firstMissingPositive(self, arr: List[int]) -> int:
        n = len(arr)

        for i in range(n):
            while(
                1 <= arr[i] <=n and arr[arr[i]-1] != arr[i]
            ):
                cI = arr[i]-1
                arr[cI] ,arr[i] = arr[i], arr[cI]
        
        for i in range(n):
            if arr[i] != i+1:
                return i+1
        return n+1