class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        m = 0b1111

        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[i][j]: m &= 0b1110
                if mat[i][j] != target[j][n - 1 - i]: m &= 0b1101
                if mat[i][j] != target[n - 1 - i][n - 1 - j]: m &= 0b1011
                if mat[i][j] != target[n - 1 - j][i]: m &= 0b0111
                if m == 0: return False

        return m != 0
