class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific = [[0] * COLS for _ in range(ROWS)]
        atlantic = [[0] * COLS for _ in range(ROWS)]

        for i in range(ROWS):
            pacific[i][0] = 1
            atlantic[i][COLS - 1] = 1
        
        for i in range(COLS):
            pacific[0][i] = 1
            atlantic[ROWS - 1][i] = 1

        def dfs(i: int, j: int, o: str) -> None:
            
            if(o == 'pacific'):
                ocean = pacific
            else:
                ocean = atlantic
            
            
            dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] #Up, Right, Down, Left

            for di, dj in dirs:
                ni, nj = i + di, j + dj

                if(ni < 0 or ni >= ROWS or nj < 0 or nj >= COLS):
                    continue

                if(heights[ni][nj] >= heights[i][j] and ocean[ni][nj] == 0): #Water can flow
                    ocean[ni][nj] = 1
                    dfs(ni, nj, o)

            
            return

        #DFS Traversal
        for i in range(ROWS):
            for j in range(COLS):
                if(pacific[i][j] == 1):
                    dfs(i, j, 'pacific')
                if(atlantic[i][j] == 1):
                    dfs(i, j, 'atlantic')

        #Check if a tile can be reached from both oceans
        res = []

        for i in range(ROWS):
            for j in range(COLS):
                if(pacific[i][j] == 1 and atlantic[i][j] == 1):
                    res.append([i, j])
        
        return res