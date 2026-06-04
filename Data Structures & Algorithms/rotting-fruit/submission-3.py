class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        q = deque()
        total_fresh = 0

        for i in range(n):
            for j in range(m):
                if(grid[i][j] == 1):
                    total_fresh += 1
                elif(grid[i][j] == 2):
                    q.append((i, j))
        
        if(total_fresh == 0):
            return 0

        fruits_rotten = 0
        vis = set()
        time = 0
        while(len(q) > 0):
            k = len(q)
            
            while(k > 0):
                i, j = q.popleft()

                # if((i, j) in vis):
                #     continue
                
                # vis.add((i, j))

                #Up
                if(i - 1 >= 0 and grid[i - 1][j] == 1 and (i - 1, j) not in vis):
                    vis.add((i - 1, j))
                    q.append((i - 1, j))
                    fruits_rotten += 1

                #Right
                if(j + 1 < m and grid[i][j + 1] == 1 and (i, j + 1) not in vis):
                    vis.add((i, j + 1))
                    q.append((i, j + 1))
                    fruits_rotten += 1

                #Down
                if(i + 1 < n and grid[i + 1][j] == 1 and (i + 1, j) not in vis):
                    vis.add((i + 1, j))
                    q.append((i + 1, j))
                    fruits_rotten += 1

                #Left
                if(j - 1 >= 0 and grid[i][j - 1] == 1 and (i, j - 1) not in vis):
                    vis.add((i, j - 1))
                    q.append((i, j - 1))
                    fruits_rotten += 1
                
                k -= 1
            
            time += 1
        
        if(fruits_rotten == total_fresh):
            res = time - 1
        else:
            res = -1
        
        return res




