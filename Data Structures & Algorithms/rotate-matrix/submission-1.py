class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(i, n - 1 - i):
                cur_index = [i,j]
                temp = matrix[i][j]
                for k in range(4):
                    next_index = [cur_index[1], n - 1 - cur_index[0]]
                    next_val = matrix[next_index[0]][next_index[1]]
                    matrix[next_index[0]][next_index[1]] = temp
                    
                    temp = next_val
                    cur_index = next_index
        
        return
