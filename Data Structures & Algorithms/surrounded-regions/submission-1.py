class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        vis = [[0] * m for _ in range(n)]


        def dfs(i: int, j: int) -> None:
            if(vis[i][j] == 1):
                return 
            
            vis[i][j] = 1
        
            dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]] #Up, Right, Down, Left
            
            for d in dirs:
                ni = i + d[0]
                nj = j + d[1]
                if(ni >= 0 and ni < n and nj >= 0 and nj < m and board[ni][nj] == 'O'):
                    dfs(ni, nj)
            
            return


        for i in range(m):
            if(board[0][i] == 'O'):
                dfs(0, i)
        
        for i in range(m):
            if(board[n - 1][i] == 'O'):
                dfs(n - 1, i)
        
        for i in range(n):
            if(board[i][0] == 'O'):
                dfs(i, 0)
        
        for i in range(n):
            if(board[i][m - 1] == 'O'):
                dfs(i, m - 1)
        

        for i in range(n):
            for j in range(m):
                if(board[i][j] == 'O' and vis[i][j] == 0):
                    board[i][j] = 'X'
        
        return