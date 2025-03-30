class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.strip().split()
        if not arr:
            return 0
        return len(arr[-1])