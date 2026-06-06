class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        vis = set()
        pq = []
        res = float('-inf')

        #Add the initial position
        heapq.heappush(pq, (0, 0, 0)) #(height, position_x, position_y)

        #Run Dijkstra's 
        while(pq):
            h, u, v = heapq.heappop(pq)

            if((u, v) in vis):
                continue

            res = max(res, grid[u][v])
            vis.add((u, v))

            #Found the exit
            if((u, v) == (n - 1, n - 1)):
                break
            
            #We check along the path for the highest height

            #Explore the neighbours
            dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

            for d in dirs:
                nu = u + d[0]
                nv = v + d[1]

                if(nu >= 0 and nu < n and nv >= 0 and nv < m):
                    heapq.heappush(pq, (grid[nu][nv], nu, nv))
            
        #Return
        return res
