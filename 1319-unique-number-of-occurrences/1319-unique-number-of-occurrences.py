class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)

        seen = set()

        for key, value in count.items():
            if value in seen:
                return False
            else:
                seen.add(value)
        return True

        # Time : O(N)
        # Space : O(N)