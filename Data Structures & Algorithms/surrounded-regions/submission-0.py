class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        vis = [[0] * n for _ in range(m)]

        def dfs(i: int, j: int):
            
            vis[i][j] = 1

            dirs = [
                [-1, 0], #Up
                [0, 1], #Right
                [1, 0], #Down
                [0, -1] #Left
            ]

            for d in dirs:
                if(i + d[0] < m and i + d[0] >= 0 and j + d[1] < n and j + d[1] >= 0 and board[i + d[0]][j + d[1]] == 'O' and vis[i + d[0]][j + d[1]] == 0):
                    dfs(i + d[0], j + d[1])
        
            return

        #Left col
        for i in range(m):
            if(board[i][0] == 'O' and vis[i][0] == 0):
                dfs(i, 0)
        
        #Bottom row
        for i in range(n):
            if(board[m - 1][i] == 'O' and vis[m - 1][i] == 0):
                dfs(m - 1, i)
        
        #Right col
        for i in range(m):
            if(board[i][n - 1] == 'O' and vis[i][n - 1] == 0):
                dfs(i, n - 1)
        
        #Top row
        for i in range(n):
            if(board[0][i] == 'O' and vis[0][i] == 0):
                dfs(0, i)
        

        # print(vis)
        for i in range(m):
            for j in range(n):
                if(vis[i][j] != 1 and board[i][j] == 'O'):
                    board[i][j] = 'X'

        return
