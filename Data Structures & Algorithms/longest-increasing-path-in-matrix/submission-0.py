class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        res = [[1] * n for _ in range(m)]

        d = {}
        unique_nums = []

        for i in range(m):
            for j in range(n):
                if(matrix[i][j] in d):
                    d[matrix[i][j]].append([i, j])
                else:
                    d[matrix[i][j]] = [[i, j]]
                    unique_nums.append(matrix[i][j])
        
        unique_nums.sort()
        final = -1

        for i in range(len(unique_nums) - 1, -1, -1):
            num = unique_nums[i]
            # print(d[num])
            for x, y in d[num]:

                #Up
                up, right, down, left = -1, -1, -1, -1
                if(x - 1 >= 0 and matrix[x - 1][y] > matrix[x][y]):
                    up = res[x - 1][y] + 1

                #Right
                if(y + 1 < n and matrix[x][y + 1] > matrix[x][y]):
                    right = res[x][y + 1] + 1

                #Down
                if(x + 1 < m and matrix[x + 1][y] > matrix[x][y]):
                    down = res[x + 1][y] + 1

                #Left
                if(y - 1 >= 0 and matrix[x][y - 1] > matrix[x][y]):
                    left = res[x][y - 1] + 1
                
                res[x][y] = max(up, right, down, left, res[x][y])
                final = max(final, res[x][y])
        
        return final
