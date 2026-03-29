class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        vis = [[0] * n for _ in range(m)]

        res = 0

        def dfs(i: int, j: int) -> None:
            # if(grid[i][j] == "0"):
            #     return

            vis[i][j] = 1

            #Up
            if(i - 1 >= 0 and grid[i - 1][j] == "1" and vis[i - 1][j] == 0):
                dfs(i-1, j)

            #Right
            if(j + 1 < n and grid[i][j + 1] == "1" and vis[i][j + 1] == 0):
                dfs(i, j + 1)

            #Down
            if(i + 1 < m and grid[i + 1][j] == "1" and vis[i + 1][j] == 0):
                dfs(i + 1, j)

            #Left
            if(j - 1 >= 0 and grid[i][j - 1] == "1" and vis[i][j - 1] == 0):
                dfs(i, j - 1)
            
            return
        
        for i in range(m):
            for j in range(n):
                if(vis[i][j] == 0 and grid[i][j] == "1"):

                    dfs(i, j)
                    res += 1

        return res