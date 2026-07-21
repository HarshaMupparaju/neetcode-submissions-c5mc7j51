class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        new_matrix = [[0] *n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                new_matrix[j][n - 1 -i] = matrix[i][j]
        
        for i in range(n):
            for j in range(n):
                matrix[i][j] = new_matrix[i][j]
            

        new_matrix = 1
        return