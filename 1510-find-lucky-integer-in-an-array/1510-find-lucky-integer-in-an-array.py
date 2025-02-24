class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)

        high = -1

        for item, value in freq.items():
            if item==value:
                high = max(value,high)
        return high