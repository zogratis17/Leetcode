class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) ==  Counter(t)
        # Time : O(N)
        # Space : O(k) k-> no of distinct char