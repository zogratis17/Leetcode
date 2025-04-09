class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        for key, val in count.items():
            if val == 1:
                return s.index(key)
        return -1

        # Time : O(N)
        # Space : O(N)