class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0

        vis = [[0] * m for _ in range(n)]

        def dfs(i: int, j: int) -> None:
            if(grid[i][j] == "0" or vis[i][j] == 1):
                return
            
            vis[i][j] = 1

            #Up
            if(i - 1 >= 0):
                dfs(i - 1, j)

            #Right
            if(j + 1 < m):
                dfs(i, j + 1)

            #Down
            if(i + 1 < n):
                dfs(i + 1, j)

            #Left
            if(j - 1 >= 0):
                dfs(i, j - 1)

            return

        for i in range(n):
            for j in range(m):
                if(grid[i][j] == "1" and vis[i][j] == 0):
                    dfs(i, j)
                    res += 1
        
        return res