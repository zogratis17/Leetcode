class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m , n = len(matrix) , len(matrix[0])

        row, column = set() , set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row.add(i)
                    column.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in row or j in column:
                    matrix[i][j] = 0