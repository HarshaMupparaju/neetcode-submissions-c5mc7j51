class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #TC: O(nm); SC: O(1)
        ROWS = len(grid)
        COLS = len(grid[0])


        vis = set()
        res = 0

        def dfs(i: int, j: int) -> None:
            if(i < 0 or i >= ROWS or j < 0 or j >= COLS or (i, j) in vis or grid[i][j] == '0'):
                return
            
            vis.add((i, j))

            #Up
            dfs(i - 1, j)

            #Right
            dfs(i, j + 1)

            #Down
            dfs(i + 1, j)

            #Left
            dfs(i, j - 1)

            return
            
        for i in range(ROWS):
            for j in range(COLS):
                if(grid[i][j] == '1' and (i, j) not in vis):
                    res += 1
                    dfs(i, j)
        
        return res
