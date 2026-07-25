class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #Dijkstra's
        ROWS = len(grid)
        COLS = len(grid[0])

        res = float('-inf')

        min_hp = []
        vis = set()

        heapq.heappush(min_hp, (grid[0][0], 0, 0)) #height, i, j

        while(len(min_hp) > 0):
            height, i, j = heapq.heappop(min_hp)


            if((i, j) in vis):
                continue
            
            vis.add((i, j))

            res = max(res, height)

            if(i == ROWS - 1 and j == COLS - 1):
                break

            #Explore neighbours
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dr, dc in dirs:
                nr, nc = i + dr, j + dc
                if(nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS):
                    heapq.heappush(min_hp, (grid[nr][nc], nr, nc))

        return res