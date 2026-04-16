class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        vis = [[0] * n for _ in range(m)]
        q = deque()

        num_fruits = 0

        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 2):
                    q.append([i, j])
                    vis[i][j] = 1
                elif(grid[i][j] == 1):
                    num_fruits += 1
        
        if(num_fruits == 0):
            return 0

        time = 0
        fruits_found = 0
        while(len(q) != 0):
            temp = len(q)
            print(q)
            
            
            
            for i in range(temp):
                front = q.popleft()
                dirs = [
                    [-1, 0], #up
                    [0, 1], #right
                    [1, 0], #bottom
                    [0, -1], #left
                ]

                for d in dirs:
                    new_dir = [front[0] + d[0], front[1] + d[1]]
                    if(new_dir[0] < m and new_dir[0] >= 0 and new_dir[1] < n and new_dir[1] >= 0 and vis[new_dir[0]][new_dir[1]] == 0 and grid[new_dir[0]][new_dir[1]] == 1):
                        vis[new_dir[0]][new_dir[1]] = 1
                        q.append(new_dir)
                        fruits_found += 1
                
            time += 1
        
        res = -1

        print(num_fruits)
        print(fruits_found)
        if(num_fruits == fruits_found):
            res = time - 1

        return res