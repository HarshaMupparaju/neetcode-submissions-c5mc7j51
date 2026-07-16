class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        vis = set()
        def dfs(i: int, j: int) -> None:

            if(i < 0 or j < 0 or i >= ROWS or j >= COLS or (i, j) in vis or board[i][j] == 'X'):
                return
            
            vis.add((i, j))
            board[i][j] = '#'

            dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] #Up, Right, Down, Left

            for di, dj in dirs:
                ni, nj = i + di, j + dj
                dfs(ni, nj)
            
            return

        for i in range(ROWS):
            if(board[i][0] == 'O'):
                dfs(i, 0)
            
            if(board[i][COLS - 1] == 'O'):
                dfs(i, COLS - 1)
            
        
        for i in range(COLS):
            if(board[0][i] == 'O'):
                dfs(0, i)
            
            if(board[ROWS - 1][i] == 'O'):
                dfs(ROWS - 1, i)
        

        for i in range(ROWS):
            for j in range(COLS):
                if(board[i][j] == 'O'):
                    board[i][j] = 'X'
                elif(board[i][j] == '#'):
                    board[i][j] = 'O'
        
        return