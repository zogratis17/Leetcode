class Solution:
    def largestSquareArea(self, bl: List[List[int]], tr: List[List[int]]) -> int:
        s = 0
        n = len(bl)

        for i in range(n):
            for j in range(i + 1, n):
                minX = max(bl[i][0], bl[j][0])
                maxX = min(tr[i][0], tr[j][0])
                minY = max(bl[i][1], bl[j][1])
                maxY = min(tr[i][1], tr[j][1])

                if minX < maxX and minY < maxY:
                    length = min(maxX - minX, maxY - minY)
                    s = max(s, length)

        return s * s
