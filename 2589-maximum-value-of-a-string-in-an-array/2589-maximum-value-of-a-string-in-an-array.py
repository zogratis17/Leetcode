class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maxVal = 0

        for s in strs:
            if s.isdigit():
                maxVal = max(int(s), maxVal)
            else:
                maxVal = max(len(s), maxVal)
        return maxVal