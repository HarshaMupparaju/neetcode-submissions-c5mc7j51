class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        transpose_matrix = [[0] * ROWS for _ in range(COLS)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                transpose_matrix[j][i] = matrix[i][j]
        
        return transpose_matrix