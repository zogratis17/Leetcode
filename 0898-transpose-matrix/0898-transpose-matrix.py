class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        rows = len(matrix)
        cols = len(matrix[0])
        
        transposed = [[0] * rows for _ in range(cols)]
        
        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = matrix [i][j]
                
        return transposed

        # Time complexity: O(m * n)
        # Space complexity: O(m * n)