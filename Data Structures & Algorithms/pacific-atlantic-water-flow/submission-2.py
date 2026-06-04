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

            #Up
            if(i - 1 >= 0 and heights[i][j] <= heights[i - 1][j]):
                dfs(i - 1 , j, ocean)

            #Right
            if(j + 1 < m and heights[i][j] <= heights[i][j + 1]):
                dfs(i, j + 1, ocean)

            #Down
            if(i + 1 < n and heights[i][j] <= heights[i + 1][j]):
                dfs(i + 1, j, ocean)

            #Left
            if(j - 1 >= 0 and heights[i][j] <= heights[i][j - 1]):
                dfs(i, j - 1, ocean)

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