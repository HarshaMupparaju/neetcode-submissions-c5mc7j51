class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])

        pacific = [[0] * m for _ in range(n)]
        atlantic = [[0] * m for _ in range(n)]

        res = []

        #Pacific
        vis = set()

        def dfs(i: int, j: int, ocean: str) -> None:
            if(ocean == 'pacific'):
                temp = pacific
            else:
                temp = atlantic
            
            if((i, j) in vis):
                return
            
            vis.add((i, j))
            temp[i][j] = 1

            dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]] # Up, Right, Down, Left

            for d in dirs:
                ni = i + d[0]
                nj = j + d[1]
                if(ni >= 0 and ni < n and nj >= 0 and nj < m and heights[i][j] <= heights[ni][nj]):
                    dfs(ni, nj, ocean)

            return


        for i in range(m):
            pacific[0][i] = 1
        
        for i in range(n):
            pacific[i][0] = 1
        
        for i in range(n):
            for j in range(m):
                if(pacific[i][j] == 1 and (i, j) not in vis):
                    dfs(i, j, 'pacific')
        

        #Atlantic
        vis = set()

        for i in range(m):
            atlantic[n - 1][i] = 1
        
        for i in range(n):
            atlantic[i][m - 1] = 1
        
        for i in range(n):
            for j in range(m):
                if(atlantic[i][j] == 1 and (i, j) not in vis):
                    dfs(i, j, 'atlantic')



        for i in range(n):
            for j in range(m):
                if(pacific[i][j] == 1 and atlantic[i][j] == 1):
                    res.append([i, j])

        return res