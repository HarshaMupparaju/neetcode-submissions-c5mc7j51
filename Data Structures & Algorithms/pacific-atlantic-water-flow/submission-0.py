class Solution:


    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pacific = [[0] * n for _ in range(m)]
        # pacific_vis = [[0] * n for _ in range(m)]

        atlantic = [[0] * n for _ in range(m)]
        # atlantic_vis = [[0] * n for _ in range(m)]


        def dfs(i: int, j: int, visit: List[List[int]], prev_height: int):
            if( i < 0 or i >= m or j < 0 or j >= n or visit[i][j] == 1 or  heights[i][j] < prev_height):
                return
            
            visit[i][j] = 1

            #Up
            dfs(i - 1, j, visit, heights[i][j])

            #Right
            dfs(i, j + 1, visit, heights[i][j])

            #Down
            dfs(i + 1, j, visit, heights[i][j])

            #Left
            dfs(i, j - 1, visit, heights[i][j])

            return


        # #Mark Cols
        # for i in range(m):
        #     pacific[i][0] = 1
        #     atlantic[i][-1] = 1

        # #Mark Rows
        # for i in range(n):
        #     pacific[0][i] = 1
        #     atlantic[-1][i] = 1
        
        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, n - 1, atlantic, heights[i][n - 1])

        for i in range(n):
            dfs(0, i, pacific, heights[0][i])
            dfs(m -1, i, atlantic, heights[m - 1][i])
    
        res = []

        for i in range(m):
            for j in range(n):
                if(pacific[i][j] == 1 and atlantic[i][j] == 1):
                    res.append([i, j])

        return res