class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [s.index(c) for c in s] == [t.index(d) for d in t]

        # Time : O(N)
        # Space : O(N)