class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        a = ma = mi = 0

        for d in differences:
            a +=d
            ma = max(ma,a)
            mi = min(mi,a)
        return max(0, (upper-lower) - (ma - mi)+1)

        # Time : O(n)
        # Space : O(1)