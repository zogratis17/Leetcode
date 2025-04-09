class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])

        # Time : O(N)
        # Space : O(1   )