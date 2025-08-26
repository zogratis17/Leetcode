class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_d = 0
        max_a = 0

        for x, y in dimensions:
            d = x ** 2 + y ** 2
            a = x * y

            if d == max_d:
                max_a = max(max_a, a)
                continue

            if d > max_d:
                max_d = d
                max_a = a

        return max_a