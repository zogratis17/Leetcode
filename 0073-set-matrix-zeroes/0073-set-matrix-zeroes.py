class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m, n = len(matrix), len(matrix[0])
        dx, dy = set(), set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dx.add(i)
                    dy.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in dx or j in dy:
                    matrix[i][j] = 0

        # Time : O(MxN)
        # space : O(M+N)
    