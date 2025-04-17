class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]

        for i in range(len(s)):
            if s.startswith(rev[i:]):
                return rev[:i]+s
        return s

        # Time : O(N^2)
        # Space : O(N)