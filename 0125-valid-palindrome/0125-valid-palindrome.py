class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = "".join([char.lower() for char in s if char.isalnum()])
    
        return check == check[::-1]
         # Time : O(N)
         # Space : O(N)