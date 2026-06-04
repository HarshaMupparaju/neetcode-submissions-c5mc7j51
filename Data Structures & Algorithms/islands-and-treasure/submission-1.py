class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])

        q = deque()

        INF = 2147483647

        for i in range(n):
            for j in range(m):
                if(grid[i][j] == 0):
                    q.append((i, j, 0))


        while(len(q) > 0):
            i, j, dist = q.popleft()
            if(grid[i][j] > dist):
                grid[i][j] = dist

            #Up
            if(i - 1 >= 0 and grid[i - 1][j] == INF):
                q.append((i - 1, j, dist + 1))
            #Right
            if(j + 1 < m and grid[i][j + 1] == INF):
                q.append((i, j + 1, dist + 1))

            #Down
            if(i + 1 < n and grid[i + 1][j] == INF):
                q.append((i + 1, j, dist + 1))

            #Left        
            if(j - 1 >= 0 and grid[i][j - 1] == INF):
                q.append((i, j - 1, dist + 1))

        return