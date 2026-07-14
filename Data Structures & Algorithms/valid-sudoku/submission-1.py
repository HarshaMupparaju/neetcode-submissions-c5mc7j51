class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #Validate Rows
        for i in range(len(board)):
            s = set()
            for j in range(len(board[0])):
                if(board[i][j] != '.'):
                    if(board[i][j] in s):
                        return False
                    s.add(board[i][j])
        
        #Validate Cols
        for i in range(len(board[0])):
            s = set()
            for j in range(len(board)):
                if(board[j][i] != '.'):
                    if(board[j][i] in s):
                        return False
                    s.add(board[j][i])

        #Validate 3x3 grids

        for n in range(len(board) // 3): # n = 0, 1, 2
            for m in range(len(board[0]) // 3): # m = 0, 1, 2
                s = set()
                for i in range(len(board) // 3): # i = 0, 1, 2
                    for j in range(len(board[0]) // 3): # j = 0, 1, 2
                        if(board[n * (len(board) // 3) + i][m * (len(board[0]) // 3) + j] != '.'):
                            if(board[n * (len(board) // 3) + i][m * (len(board[0]) // 3) + j] in s):
                                return False
                            s.add(board[n * (len(board) // 3) + i][m * (len(board[0]) // 3) + j])
        
        return True
