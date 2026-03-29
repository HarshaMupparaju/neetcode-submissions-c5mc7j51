class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_row = 1

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if(matrix[i][j] == 0):
                    if(i == 0):
                        zero_row = 0
                    else:
                        matrix[i][0] = 0
                    
                    matrix[0][j] = 0
        
        print(matrix[0])
        print(zero_row)





            
        
        #Iterate cols
        for i in range(1, n):
            if(matrix[0][i] == 0):
                for j in range(m):
                    matrix[j][i] = 0
        
        # Iterate rows
        for i in range(1, m):
            if(matrix[i][0] == 0):
                for j in range(n):
                    matrix[i][j] = 0
        
        #Iterate 1 col
        if(matrix[0][0] == 0):
            for j in range(m):
                matrix[j][0] = 0
        
        #Iterate 1 row
        if(zero_row == 0):
            for j in range(n):
                matrix[zero_row][j] = 0

        return
        

        