class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        vis = [[0] * m for _ in range(n)]


        def dfs(i: int, j: int) -> int:
            if(grid[i][j] == 0 or vis[i][j] == 1):
                return 0
            
            vis[i][j] = 1

            temp = 0
            #Up
            if(i - 1 >= 0):
                up = dfs(i - 1, j)
                temp += up

            #Right
            if(j + 1 < m):
                right = dfs(i, j + 1)
                temp += right

            #Down
            if(i + 1 < n):
                down = dfs(i + 1, j)
                temp += down

            #Left
            if(j - 1 >= 0):
                left = dfs(i, j - 1)
                temp += left

            return 1 + temp

        res = 0
        for i in range(n):
            for j in range(m):
                if(grid[i][j] == 1 and vis[i][j] == 0):
                    res = max(res, dfs(i, j))
        
        return res