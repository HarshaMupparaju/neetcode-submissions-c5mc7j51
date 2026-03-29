class Solution:
    def isInvalid(self, temp:List[str]) -> bool:
        d = {}
        for i in range(len(temp)):
            if(temp[i] != '.'):
                if(temp[i] in d):
                    return True
                else:
                    d[temp[i]] = 1
        
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(board[i][j])
            if(self.isInvalid(temp)):
                return False
        
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(board[j][i])
            if(self.isInvalid(temp)):
                return False
        
        for i in range(m // 3):
            for j in range(n // 3):
                temp = []
                for k in range(3):
                    for l in range(3):
                        temp.append(board[i * 3 + k][j * 3 + l])
                if(self.isInvalid(temp)):
                    return False
        
        return True