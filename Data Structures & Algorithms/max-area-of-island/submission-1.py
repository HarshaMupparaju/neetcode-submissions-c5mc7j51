class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        n = len(grid)
        m = len(grid[0])

        vis = [[0] * m for _ in range(n)]

        def dfs(i: int, j: int) -> int:
            if(i >= n or i < 0 or j >= m or j < 0 or vis[i][j] == 1 or grid[i][j] == 0):
                return 0 
            
            vis[i][j] = 1

            #Up
            up =  dfs(i - 1, j)

            #Right
            right = dfs(i, j + 1)

            #Left
            left = dfs(i, j - 1)

            #Down
            down = dfs(i + 1, j)

            return (1 + up + right + left + down)

        for i in range(n):
            for j in range(m):
                if(grid[i][j] == 1):
                    res = max(res, dfs(i, j))

        return res