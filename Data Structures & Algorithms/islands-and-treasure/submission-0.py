class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        INF = 2147483647

        vis = [[0] * n for _ in range(m)]

        q = deque()

        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 0):
                    vis[i][j] = 1
                    q.append((i, j))
        
        while(len(q) != 0):
            front = q.popleft()
            i = front[0]
            j = front[1]

            # vis[i][j] = 1
            dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

            for d in dirs:
                if(i + d[0] < 0 or i + d[0] >= m or j + d[1] < 0 or j + d[1] >= n or vis[i + d[0]][j + d[1]] == 1 or grid[i + d[0]][j + d[1]] == -1):
                    continue
                
                grid[i + d[0]][j + d[1]] = grid[i][j] + 1
                vis[i + d[0]][j + d[1]] = 1

                q.append([i + d[0], j + d[1]])

        return 